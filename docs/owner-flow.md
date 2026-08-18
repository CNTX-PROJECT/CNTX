# OWNER-flow en taakgates

[Documentatie-index](README.md) · [Workspace](workspace.md) ·
[Commandoreferentie](commands.md) · [Security](security.md)

De workspaceflow maakt één lokale taak controleerbaar van voorstel tot
sluiting. OPENCNTX registreert overgangen en digests, maar voert de inhoudelijke
taak niet zelf uit.

## Rollen en vaste volgorde

```text
OWNER-doel
→ ARCHITECT-analyse
→ ARCHITECT-voorstel met exacte inputs en grenzen
→ afzonderlijke OWNER-goedkeuring van het voorstel
→ begrensde uitvoering
→ resultaat en bewijs
→ ARCHITECT-review
→ afzonderlijke OWNER-aanvaarding van exact resultaat en review
→ taaksluiting
```

De waarden bij `--owner`, `--architect` en `--executor` zijn lokale
actorverklaringen. Zonder account, sleutel of digitale handtekening bewijst
OPENCNTX niet welke natuurlijke persoon het commando invoerde.

## 1. Playbook en rol voorbereiden

Een playbook beschrijft een herhaalbare werkwijze. Een rol beschrijft de vaste
grenzen van één tijdelijke uitvoerder. Registratie maakt uitsluitend een
`PROPOSED` definitie en start niets:

```powershell
opencntx workspace playbook register PB-BRON-CONTROLE `
  --revision 1 `
  --title "Controleer één bron" `
  --purpose "Controleer uitsluitend de toegewezen bron." `
  --input "Eén taakgebonden contextpakket" `
  --step "Controleer eerst alle digests." `
  --stop "Stop bij ontbrekende of gewijzigde bronbytes." `
  --evidence "Exacte bron-ID, revisie en SHA-256." `
  --allow inspect-source `
  --allow write-bounded-result `
  --forbid external-send `
  --forbid subdelegate `
  --architect ARCHITECT `
  --root mijn-project
```

Een rol moet alle vaste authority-acties verbieden, waaronder OWNER-
goedkeuring, taaksluiting, roadmapwijziging, subdelegatie, merge, release,
publicatie, verwijdering en externe verzending. Delegatiediepte is exact één en
`may_delegate` blijft altijd false.

Gebruik daarna de getoonde definitiedigests om playbook en rol afzonderlijk
goed te keuren:

```powershell
opencntx workspace playbook approve PB-BRON-CONTROLE `
  --revision 1 `
  --definition-digest <EXACTE-PLAYBOOKDIGEST> `
  --owner OWNER `
  --root mijn-project

opencntx workspace role approve ROLE-BRON-REVIEWER `
  --revision 1 `
  --definition-digest <EXACTE-ROLDIGEST> `
  --owner OWNER `
  --root mijn-project
```

Een nieuwe inhoudelijke definitie krijgt een nieuwe revisie en bindt met
`--supersedes-digest` aan de vorige definitiedigest. Oude revisies en approvals
worden niet overschreven.

## 2. Taak voorstellen

Een taakvoorstel pint minimaal één officieel inputbestand, toegestane en
verboden acties, verwacht resultaat en acceptatiecriterium:

```powershell
opencntx workspace task propose TASK-20260818-0001 `
  --title "Controleer één bron" `
  --goal "Controleer de bron tegen het goedgekeurde hoofdstuk." `
  --done "Resultaat bevat afwijkingen, bewijs en open vragen." `
  --executor-role ROLE-BRON-REVIEWER `
  --input CONTROL/OWNER.md `
  --input CONTROL/ROADMAP.md `
  --input CONTROL/CURRENT.md `
  --input CHAPTERS/CH-BRON/CHAPTER.md `
  --input PLAYBOOKS/PB-BRON-CONTROLE/r0001/PLAYBOOK.md `
  --input ROLES/ROLE-BRON-REVIEWER/r0001/ROLE.md `
  --allow inspect-source `
  --allow write-bounded-result `
  --forbid external-send `
  --expected-output "Eén lokaal resultaat met bewijs" `
  --acceptance "Iedere claim verwijst naar een gepinde input" `
  --architect ARCHITECT `
  --root mijn-project
```

Het voorstel toont de exacte proposal-digest. OPENCNTX staat maximaal één
niet-terminale taak tegelijk toe.

## 3. Voorstel afzonderlijk goedkeuren en beginnen

```powershell
opencntx workspace task approve TASK-20260818-0001 `
  --revision 1 `
  --proposal-digest <EXACTE-VOORSTELDIGEST> `
  --owner OWNER `
  --root mijn-project

opencntx workspace task begin TASK-20260818-0001 `
  --architect ARCHITECT `
  --root mijn-project
```

`begin` registreert alleen `IN_EXECUTION` en maakt een kleine leesbare
`TASK.md`. Het start geen mens, AI, agent, shell of ander proces.

Taakevents onder `TASKS/<TASK-ID>/events/` zijn append-only en aan elkaar
gehasht. Een gewijzigd event, oude digest, ontbrekende input, handmatig
gewijzigde taakkaart of overgeslagen status wordt geweigerd.

## 4. Catalogus en levende context controleren

Herbouw de catalogus na de laatste officiële bron- of hoofdstukwijziging:

```powershell
opencntx workspace catalog rebuild --root mijn-project
```

De contextnavigator werkt alleen voor een valide taak exact in
`IN_EXECUTION`. `CONTROL/OWNER.md`, `CONTROL/ROADMAP.md` en
`CONTROL/CURRENT.md` moeten als taakinputs gepind zijn. `CURRENT.md` moet de
actieve taak en revisie noemen. Alle relevante hoofdstukken moeten
`OWNER_ACCEPTED` en technisch `CURRENT` zijn.

Een nieuwe werkruimte heeft in `ROADMAP.md` één exact gemarkeerd actueel block.
U kunt de afgeleide snapshot vooraf zichtbaar vernieuwen:

```powershell
opencntx workspace control refresh --root mijn-project
```

`context build` doet deze refresh in compact mode ook automatisch. De taak pint
nog steeds de volledige `ROADMAP.md`; het manifest bewaart haar volledige
SHA-256. Alleen de byte-exacte actuele sectie komt als hete snapshot in
`CONTEXT.md`. Zonder markers blijft de volledige roadmaproute actief.

```powershell
opencntx workspace context build TASK-20260818-0001 `
  --proposal-digest <EXACTE-VOORSTELDIGEST> `
  --max-files 25 `
  --max-bytes 100000 `
  --root mijn-project

opencntx verify mijn-project/.opencntx/latest

opencntx workspace context verify TASK-20260818-0001 `
  --proposal-digest <EXACTE-VOORSTELDIGEST> `
  --root mijn-project
```

De selectie volgt uitsluitend expliciete taakinputs, hoofdstukafhankelijkheden
en bronpins. De vaste laadvolgorde is heet — CONTROL en taak; warm —
hoofdstukken, playbooks en rollen; koud — hun gepinde bronrecords en
UTF-8-originelen. `QUARANTINED` wordt geweigerd; `RESTRICTED` vereist een
expliciete broninput. Een te klein budget maakt geen gedeeltelijk pakket. Een
beschadigde markerconfiguratie valt nooit stil terug naar legacy mode.

## 5. Eén begrensd uitvoerderpakket

Na groene levende contextcontrole kan één pakket worden voorbereid:

```powershell
opencntx workspace executor prepare TASK-20260818-0001 `
  --revision 1 `
  --proposal-digest <EXACTE-VOORSTELDIGEST> `
  --playbook-id PB-BRON-CONTROLE `
  --playbook-revision 1 `
  --playbook-digest <EXACTE-PLAYBOOKDIGEST> `
  --role-id ROLE-BRON-REVIEWER `
  --role-revision 1 `
  --role-digest <EXACTE-ROLDIGEST> `
  --context-manifest-digest <EXACTE-CONTEXTMANIFESTDIGEST> `
  --executor UITVOERDER-1 `
  --root mijn-project
```

Het pakket bevat `ASSIGNMENT.md` en een exact record, maar kopieert geen bron-
of contextbytes. Toegestane acties moeten tegelijk door taak, playbook en rol
zijn toegestaan; verboden wint altijd. Het pakket verleent geen computer-,
bestands- of netwerktoegang en start niets.

## 6. Verplichte verificatie vóór resultaatindiening

Voer de twee levende controles uit terwijl de taak nog `IN_EXECUTION` is:

```powershell
opencntx verify mijn-project/.opencntx/latest
opencntx workspace context verify TASK-20260818-0001 `
  --proposal-digest <EXACTE-VOORSTELDIGEST> `
  --root mijn-project
```

Dit gebeurt na contextbouw en vóór `workspace task submit-result`. Na
resultaatindiening of taaksluiting is het pakket geen levende uitvoeringsroute
meer. Deze volgorde voorkomt dat een historische snapshot ten onrechte als
actuele `IN_EXECUTION`-context wordt voorgesteld.

## 7. Resultaat, review, OWNER-besluit en sluiting

Gebruik achtereenvolgens:

1. `workspace task submit-result` voor één resultaat en optionele
   bewijsbestanden;
2. `workspace task review-result` voor de ARCHITECT-controle van de exacte
   resultaatdigest;
3. `workspace task accept-result` voor een afzonderlijk OWNER-besluit over de
   exacte resultaat- en reviewdigests;
4. `workspace task close` alleen na OWNER-`ACCEPT`.

Resultaat en bewijs blijven onvertrouwde bytes en worden niet uitgevoerd of
geïnterpreteerd. Gebruik bij ieder commando de digests die de vorige stap
letterlijk heeft getoond; raadpleeg `--help` voor alle argumenten.

## Historische controle na sluiting

Na `CLOSED` controleert u niet opnieuw een levende contextstatus. Gebruik:

- `workspace task status` voor de volledige append-only taakketen;
- de gepinde voorstel-, input-, resultaat-, review- en acceptatiedigests;
- het opgeslagen resultaat en bewijs;
- `workspace executor status` en `workspace executor verify`.

Het enige uitvoerderpakket hoort dan uitsluitend `TASK_FINISHED` te melden.
Een gesloten snapshot blijft bewijs van wat werd gebruikt, maar is geen nieuwe
uitvoeringsbevoegdheid.

## Fail-closed en anti-deadloop

OPENCNTX herhaalt geen taak automatisch. Handmatige fouten kunnen met
`workspace task record-attempt` worden geregistreerd. Na drie opeenvolgende
gelijke foutsignaturen wordt de taak zichtbaar `BLOCKED`. Verder uitvoeren of
via een nieuw uitvoerderpakket omzeilen is dan niet toegestaan.

`RETURNED`, `BLOCKED`, `CANCELLED`, `SUPERSEDED` en een ongeldige eventketen
kunnen niet als voltooid worden gesloten. `cancel` en `supersede` zijn
expliciete terminale keuzes en geen verborgen retry.
