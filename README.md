# OPENCNTX

OPENCNTX maakt voor één AI-taak een klein, expliciet en controleerbaar
contextpakket. U kiest zelf de lokale tekstbronnen; OPENCNTX bundelt ze met
paden, groottes en SHA-256-hashes. De tool werkt zonder account, netwerk, API-key
of AI-provider.

## Versiestatus

| Versie | Inhoud | Status |
|---|---|---|
| `v0.1.0` | `init`, `pack` en `verify` | Gepubliceerde kernrelease |
| `0.2.0.dev0` op `main` | Kern plus de lokale `workspace`-groep | Ontwikkelversie; nog geen `v0.2.0`-release |

## Installeren

Vereist: Python 3.11 of nieuwer en Git voor onderstaande download. OPENCNTX
staat niet op PyPI en gebruikt de standaard Python-packageflow.

### Gepubliceerde kernrelease `v0.1.0`

```powershell
git clone --branch v0.1.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

### Actuele ontwikkelbron `0.2.0.dev0`

Gebruik deze bron alleen wanneer u ook de lokale `workspace`-groep wilt
uitproberen. Zij is nog niet als `v0.2.0` gepubliceerd:

```powershell
git clone --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

Controleer na beide installatiepaden met `opencntx --help` of de installatie
beschikbaar is.

## De drie commando's

Ga na installatie naar de bestaande of nieuwe lokale projectmap waarvoor u één
AI-taak wilt uitvoeren. Die map wordt de projectroot. Voer daar `init` uit:

```powershell
opencntx init
```

Dit maakt veilig één `opencntx.toml` en overschrijft nooit een bestaand bestand.
Vul daarin één doel en de toegestane bronnen in, bijvoorbeeld:

```toml
[task]
goal = "Leg uit waarom deze kleine Python-test faalt"

[context]
include = ["README.md", "src/**/*.py", "tests/**/*.py"]
required = ["README.md"]
exclude = [".git/**", ".env*", "**/*.key", "**/*.pem"]
max_files = 25
max_bytes = 100000
```

Maak en controleer het pakket:

```powershell
opencntx pack
opencntx verify .opencntx/latest
```

`pack` schrijft atomair exact twee primaire bestanden:

- `.opencntx/latest/CONTEXT.md` — context die u eerst leest en daarna aan een
  AI-tool kunt geven;
- `.opencntx/latest/manifest.json` — bronpaden, bytes, hashes, selectie en
  uitsluitredenen.

`verify` toont `unchanged`, `changed`, `missing` en `unexpected` afzonderlijk.
Exitcode `0` betekent gelijk, `1` betekent drift of een onvolledige controle en
`2` betekent een configuratie- of uitvoerfout.

## Optioneel lokaal opslagfundament

> De `workspace`-groep zit in de actuele bronversie `0.2.0.dev0` op `main`, maar
> niet in de gepubliceerde tag `v0.1.0`. Een definitieve `v0.2.0`-release is nog
> niet gepubliceerd.

De optionele `workspace`-groep maakt een gewone lokale projectwerkruimte en kan
één aangeleverd bestand veilig registreren zonder het uit te voeren of te
interpreteren:

```powershell
opencntx workspace init mijn-project
opencntx workspace capture plan.pdf --root mijn-project --origin OWNER
```

`workspace init` maakt leesbare mappen voor besturing, inbox, bronnen,
hoofdstukken, taken, werkwijzen en rollen. Een bestaande volledige werkruimte
wordt niet herschreven; een gedeeltelijke of conflicterende structuur wordt
geweigerd.

`workspace capture`:

- accepteert precies één regulier lokaal bestand;
- bewaart de exacte bytes onder een unieke source-ID;
- registreert grootte, SHA-256, UTC-tijd, herkomst en privacy;
- gebruikt standaard privacylabel `PRIVATE`;
- herkent een exacte duplicaat zonder een tweede bronkopie te maken;
- verwijdert, verplaatst, opent of voert het aangeleverde bestand niet uit;
- eindigt zichtbaar als `CAPTURED`, `DUPLICATE` of `NOT_CAPTURED`;
- schrijft een klein ontvangstbewijs onder `.opencntx/receipts/`.

Beschikbare privacylabels zijn `PUBLIC`, `PRIVATE`, `RESTRICTED` en
`QUARANTINED`. Met `--supersedes SOURCE-ID` kan een nieuwe inhoudsversie
expliciet naar een bestaande bron verwijzen.

Na capture kan één duidelijk onderwerp een uniform, nog niet goedgekeurd
hoofdstuk krijgen. Met `--source` wordt de exacte geregistreerde SHA-256 in het
hoofdstuk vastgezet; de optie mag voor meerdere bronnen worden herhaald:

```powershell
opencntx workspace chapter create CH-ELEKTRICITEIT `
  --title "Elektriciteit" `
  --source SRC-20260816-0123456789ab `
  --root mijn-project
opencntx workspace catalog rebuild --root mijn-project
```

`chapter create` maakt uitsluitend
`CHAPTERS/CH-ELEKTRICITEIT/CHAPTER.md` als leesbaar `DRAFT`-sjabloon. Het
overschrijft geen bestaand hoofdstuk en verleent geen OWNER-goedkeuring. Met
herhaalbare `--depends-on CHAPTER-ID`-opties kunnen bestaande hoofdstukken als
afhankelijkheid worden vastgelegd.

`catalog rebuild`:

- leest alleen officiële bronrecords en `CHAPTER.md`-bestanden;
- controleert bronbytes en exacte hashpins zonder broninhoud te interpreteren;
- berekent `CURRENT`, `STALE`, `INCOMPLETE` of `ARCHIVED`;
- regenereert de compacte menselijke `CHAPTERS/INDEX.md`;
- vervangt `.opencntx/catalog.sqlite` na SQLite-integriteitscontrole;
- schrijft een rebuildreceipt en toont dezelfde state-digest in index en
  catalogus;
- stopt bij onveilige paden, dubbele ID's, onbekende formaten of een
  dependencycyclus.

De Markdown-bronnen en hoofdstukken blijven officieel. `INDEX.md` en SQLite
bevatten geen unieke waarheid en kunnen volledig opnieuw worden opgebouwd. Een
technische freshnessstatus is geen inhoudelijke waarheid of OWNER-goedkeuring.
De catalogus bevat geen originele bronbytes, volledige samenvattingen,
embeddings of vectoren.

### Media en veilige afgeleide tekst

`workspace capture` bewaart afbeeldingen, schema's, PDF's, audio en video al
byte-exact zonder ze uit te voeren. OPENCNTX start zelf geen OCR, transcriptie,
parser of AI. Wanneer een mens of een afzonderlijk gekozen hulpmiddel een
UTF-8-tekstbestand heeft gemaakt, kan die tekst wel veilig en zichtbaar als
afleiding worden geregistreerd:

```powershell
opencntx workspace media register SRC-20260817-0123456789ab `
  --text afgeleid.txt `
  --kind OCR `
  --producer-class LOCAL_TOOL `
  --producer "offline-tool 1" `
  --locator "pagina 1-3" `
  --root mijn-project
```

De registratie bewaart `content.txt` en een onveranderlijk record onder
`.opencntx/derived/<SOURCE-ID>/<DERIVATION-ID>/`. Het record bindt de tekst aan
de exacte originele bron- en recordhash, erft het privacylabel en bewaart de
opgegeven soort, makerklasse en locators. Deze metadata is een lokale
verklaring; OPENCNTX bewijst niet welk hulpmiddel de tekst werkelijk maakte.

`workspace media status` toont altijd een expliciete toestand:

- `NOT_INVESTIGATED` — geen afgeleide tekst geregistreerd;
- `UNREVIEWED` — geregistreerd maar niet menselijk gecontroleerd;
- `REVIEWED` — bruikbaar bevonden, maar niet automatisch een feit;
- `REJECTED` — afgewezen en niet promoveerbaar;
- `PROMOTED` — bewust als gewone `CAPTURED` tekstbron opgeslagen;
- `STALE` — originele of afgeleide bytes wijken af;
- `REMOVED` — afgeleide tekstkopie verwijderd, provenance bewaard.

Een controle bindt de beslissing aan de exacte contentdigest:

```powershell
opencntx workspace media review SRC-... DRV-... `
  --content-sha256 <EXACTE-64-HEX-DIGEST> `
  --decision ACCEPT `
  --finding "pagina's handmatig vergeleken" `
  --reviewer "ARCHITECT" `
  --root mijn-project
```

Alleen `REVIEWED` kan met de getoonde reviewdigest bewust worden gepromoveerd:

```powershell
opencntx workspace media promote SRC-... DRV-... `
  --review-digest <EXACTE-64-HEX-DIGEST> `
  --root mijn-project
opencntx workspace media verify SRC-... DRV-... --root mijn-project
```

Promotie gebruikt de bestaande veilige captureflow en maakt uitsluitend een
gewone tekstbron met dezelfde privacy en een exacte verwijzing naar origineel
en afleiding. De tekst wordt niet automatisch een feit, hoofdstuk,
OWNER-goedgekeurde kennis, catalogusselectie of taakcontext. Zij moet daarna
bewust door de bestaande chapter- en taskflow worden gepind.

Een nieuwe afleiding overschrijft nooit de oude; gebruik
`--supersedes-derivation-id DRV-...`. Exacte verwijdering vereist source-ID,
derivation-ID, recorddigest, contentdigest en een lokale OWNER-verklaring:

```powershell
opencntx workspace media remove SRC-... DRV-... `
  --record-digest <EXACTE-64-HEX-DIGEST> `
  --content-sha256 <EXACTE-64-HEX-DIGEST> `
  --owner "OWNER" `
  --root mijn-project
```

Dit verwijdert alleen de afgeleide `content.txt`. Het officiële origineel,
andere afleidingen en een reeds gepromoveerde bron blijven bestaan. Een klein
verwijderrecord blijft als provenance leesbaar. `status` en `verify` zijn
read-only en schrijven geen receipt.

### Begrensde taak met OWNER-gates

Eén lokale taak kan als een controleerbare keten worden vastgelegd. De normale
volgorde is:

```text
ARCHITECT-voorstel
→ exacte OWNER-goedkeuring
→ uitvoering geregistreerd
→ resultaat en bewijs ingeleverd
→ ARCHITECT-controle
→ exacte OWNER-aanvaarding
→ lokaal afrondingsbewijs
```

Begin met één voorstel dat minimaal één officieel inputbestand, toegestane
actie, verboden actie en acceptatiecriterium vastpint:

```powershell
opencntx workspace task propose TASK-20260816-0001 `
  --title "Controle elektrische offerte" `
  --goal "Controleer de offerte tegen het goedgekeurde hoofdstuk." `
  --done "Resultaat bevat afwijkingen, bewijs en open vragen." `
  --executor-role "ROLE-ELEKTRICIEN" `
  --input "CHAPTERS/CH-ELEKTRICITEIT/CHAPTER.md" `
  --allow "Lees uitsluitend de gepinde input" `
  --forbid "Geen externe verzending" `
  --expected-output "Eén lokaal resultaat met bewijs" `
  --acceptance "Iedere claim verwijst naar een gepinde input" `
  --architect "ARCHITECT" `
  --root mijn-project
```

De uitvoer toont de exacte voorstel-digest. Alleen die digest en revisie kunnen
daarna worden goedgekeurd:

```powershell
opencntx workspace task approve TASK-20260816-0001 `
  --revision 1 `
  --proposal-digest <EXACTE-64-HEX-DIGEST> `
  --owner "OWNER" `
  --root mijn-project
opencntx workspace task begin TASK-20260816-0001 `
  --architect "ARCHITECT" `
  --root mijn-project
```

`begin` registreert alleen de overgang en maakt een kleine menselijke
`TASK.md`; het start geen proces, AI of agent. `submit-result` bewaart één
resultaat en optionele bewijsbestanden uitsluitend als onvertrouwde bytes.
`review-result`, `accept-result` en `close` vereisen telkens de exacte digests
van de vorige objecten. `status` hercontroleert de volledige eventketen, inputs
en artifacts.

Taakevents onder `TASKS/<TASK-ID>/events/` zijn append-only en aan elkaar
gehasht. Een oude digest, gewijzigde input, ontbrekend bewijs, handmatig
veranderde taakkaart of overgeslagen status wordt geweigerd. Er kan maximaal één
niet-terminale taak tegelijk bestaan. OPENCNTX herhaalt nooit automatisch; de
derde opeenvolgende gelijke foutsignatuur wordt zichtbaar `BLOCKED`.

De opties `--owner`, `--architect` en `--executor` leggen een lokale
actorverklaring vast. Zonder account, sleutel of digitale handtekening bewijst
OPENCNTX niet welke natuurlijke persoon het commando invoerde. Lokale
bestandstoegang blijft de vertrouwensgrens. De workflow wijzigt geen roadmap,
`CURRENT.md`, bronnen, hoofdstukken of catalogus en voert geen taakresultaat uit.

### Taakgebonden contextnavigator

Na exacte OWNER-goedkeuring en `workspace task begin` kan de lokale navigator
voor die ene taak een normaal OPENCNTX-pakket maken. De selectie gebruikt geen
AI of vrije zoekopdracht. Zij volgt uitsluitend gepinde taakinputs,
hoofdstukafhankelijkheden en bron-ID's.

Vooraf gelden deze zichtbare voorwaarden:

- de taak is exact `IN_EXECUTION`;
- `CONTROL/OWNER.md`, `CONTROL/ROADMAP.md` en `CONTROL/CURRENT.md` zijn als
  taakinputs goedgekeurd;
- `CURRENT.md` bevat exact
  `- Actieve taak: TASK-YYYYMMDD-NNNN revisie 1`;
- minimaal één hoofdstuk, playbook, rol of geregistreerde bron is als
  inhoudelijke taakinput gepind;
- `workspace catalog rebuild` is na de laatste officiële bron- of
  hoofdstukwijziging uitgevoerd.

Bouw daarna met bewuste harde contextgrenzen:

```powershell
opencntx workspace context build TASK-20260816-0001 `
  --proposal-digest <EXACTE-64-HEX-DIGEST> `
  --max-files 25 `
  --max-bytes 100000 `
  --root mijn-project
```

De vaste laadvolgorde is:

1. **heet** — OWNER-regels, roadmap, actuele taak en taakkaart;
2. **warm** — expliciete hoofdstukken, hun afhankelijkheden, playbooks en
   rollen;
3. **koud** — exact door die route gepinde bronrecords en UTF-8-originelen.

Alle relevante hoofdstukken moeten `OWNER_ACCEPTED` en `CURRENT` zijn.
`RESTRICTED` bronnen vereisen bovendien een expliciete broninput;
`QUARANTINED`, binaire, ontbrekende en verouderde bronnen worden geweigerd.
Een te klein budget geeft een fout en laat een bestaand pakket intact: er wordt
nooit stil afgekapt of willekeurig context weggelaten.

Een succes schrijft atomair de bestaande twee primaire bestanden onder
`.opencntx/latest/`. Het gewone manifest bevat daarnaast een `navigation`-deel
met taak- en catalogusdigests, gelezen heet/warm/koud-paden en de niet-gelezen
hoofdstuk- en bron-ID's buiten de goedgekeurde taakscope.

Gebruik beide controles:

```powershell
opencntx verify .opencntx/latest
opencntx workspace context verify TASK-20260816-0001 `
  --proposal-digest <EXACTE-64-HEX-DIGEST> `
  --root mijn-project
```

De eerste controleert pakket- en bronbytes. De tweede controleert read-only ook
de actuele taakketen, CONTROL-binding, catalogus, dependencyclosure, freshness,
privacy en deterministische selectie. Een lokaal gebouwd pakket is geen
toestemming om het extern te delen en beweert nooit dat het volledige project
werd onderzocht.

Voer beide controles uit zolang de taak nog `IN_EXECUTION` is: na de contextbouw
en vóór `workspace task submit-result`. Na resultaatindiening, OWNER-aanvaarding
of taaksluiting is het pakket geen levende uitvoeringsroute meer. Controleer de
historische afronding dan via de append-only taakketen en vastgelegde digests,
het resultaat en bewijs, plus `workspace executor status` en
`workspace executor verify`. Het enige uitvoerderpakket hoort na sluiting
uitsluitend `TASK_FINISHED` te rapporteren.

De leesbare frontmatter van `CONTROL/CURRENT.md` legt standaard maximaal 2 GiB
per bron of afgeleide tekst en 20 GiB gezamenlijke officiële bron- en actieve
afgeleide tekstbytes vast. Deze opslagbudgetten staan los van de veel kleinere
contextbudgetten van `pack`.

Deze lokale werkruimtelaag doet bewust geen achtergrondbewaking, chatopname,
netwerkdownload, cloudback-up, OCR, transcriptie, beeld- of videoanalyse,
vrije zoekopdracht, AI-selectie of agentuitvoering. Mediaregistratie bewaart
alleen reeds aangeleverde afgeleide UTF-8-tekst. De SQLite-catalogus is
uitsluitend een lokale, herbouwbare metadata-index; de taakflow is uitsluitend
een lokale bewijs- en statusketen en de navigator uitsluitend een
deterministische lokale pakketroute.

### Begrensde playbooks, rollen en uitvoerderpakketten

Een playbook is een herhaalbare werkwijze; een rol beschrijft de vaste grenzen
van een tijdelijke uitvoerder. Beide beginnen als `PROPOSED` en worden pas
bruikbaar nadat de OWNER hun exacte revisie en definitie-SHA-256 afzonderlijk
heeft goedgekeurd. Registratie voert de stappen niet uit:

```powershell
opencntx workspace playbook register PB-BRON-CONTROLE `
  --revision 1 `
  --title "Controleer één bron" `
  --purpose "Controleer uitsluitend de toegewezen bron." `
  --input "Eén taakgebonden contextpakket" `
  --step "Controleer eerst alle digests." `
  --stop "Stop bij ontbrekende of gewijzigde bronbytes." `
  --evidence "Exacte bron-ID, versie en SHA-256." `
  --allow inspect-source `
  --allow write-bounded-result `
  --forbid external-send `
  --forbid subdelegate `
  --architect "ARCHITECT" `
  --root mijn-project
```

Een rol gebruikt dezelfde kleine actietokens. Zij moet alle vaste
authority-acties verbieden, waaronder `owner-approve`, `owner-accept`,
`task-close`, `roadmap-change`, `subdelegate`, `merge`, `release`, `publish`,
`delete` en `external-send`:

```powershell
opencntx workspace role register ROLE-BRON-REVIEWER `
  --revision 1 `
  --title "Begrensde bronreviewer" `
  --responsibility "Controleer uitsluitend de toegewezen bron." `
  --allow inspect-source `
  --allow write-bounded-result `
  --forbid delete `
  --forbid external-send `
  --forbid merge `
  --forbid owner-accept `
  --forbid owner-approve `
  --forbid playbook-approve `
  --forbid publish `
  --forbid release `
  --forbid roadmap-change `
  --forbid role-approve `
  --forbid subdelegate `
  --forbid task-cancel `
  --forbid task-close `
  --forbid task-supersede `
  --handoff "Lever resultaat en bewijs terug aan de ARCHITECT." `
  --architect "ARCHITECT" `
  --root mijn-project
```

Gebruik de getoonde definitiedigests om iedere revisie exact goed te keuren:

```powershell
opencntx workspace playbook approve PB-BRON-CONTROLE `
  --revision 1 `
  --definition-digest <EXACTE-PLAYBOOKDIGEST> `
  --owner "OWNER" `
  --root mijn-project
opencntx workspace role approve ROLE-BRON-REVIEWER `
  --revision 1 `
  --definition-digest <EXACTE-ROLDIGEST> `
  --owner "OWNER" `
  --root mijn-project
```

Een nieuwe inhoudelijke versie krijgt een nieuwe revisiemap en bindt met
`--supersedes-digest` exact de vorige definitiedigest. Oude revisies en
approvals worden niet overschreven. `status` en `verify` zijn read-only en
tonen `PROPOSED`, `APPROVED`, `STALE` of `INVALID`.

Voor een V6-uitvoerderpakket moet het bestaande taakvoorstel de exacte
`PLAYBOOK.md` en `ROLE.md` als inputs pinnen, het rol-ID letterlijk als
`--executor-role` gebruiken en uitsluitend kleine actietokens in `--allow` en
`--forbid` gebruiken. Nadat de taak exact `IN_EXECUTION` is en de
contextnavigator groen is, kan één pakket worden voorbereid:

```powershell
opencntx workspace executor prepare TASK-20260817-0001 `
  --revision 1 `
  --proposal-digest <EXACTE-TAAKVOORSTELDIGEST> `
  --playbook-id PB-BRON-CONTROLE `
  --playbook-revision 1 `
  --playbook-digest <EXACTE-PLAYBOOKDIGEST> `
  --role-id ROLE-BRON-REVIEWER `
  --role-revision 1 `
  --role-digest <EXACTE-ROLDIGEST> `
  --context-manifest-digest <EXACTE-CONTEXTMANIFESTDIGEST> `
  --executor "UITVOERDER-1" `
  --root mijn-project
```

`prepare` hercontroleert de volledige taakketen, inputs, context, definities,
approvals en actiegrenzen. De effectieve toegestane acties moeten zowel door de
taak als door het playbook en de rol zijn toegestaan; verboden wint altijd.
Het resultaat onder `.opencntx/executors/` is een klein `ASSIGNMENT.md` plus
een exact record. Het verwijst naar `.opencntx/latest` en kopieert geen
bron- of contextbytes.

`EXECUTOR_PACKAGE_PREPARED` betekent alleen dat de opdracht controleerbaar is
samengebonden. OPENCNTX start geen mens, proces, tool, AI of agent en verleent
geen computer- of netwerktoegang. Delegatiediepte is exact één en
`may_delegate` is altijd false. Resultaat en bewijs keren via de bestaande
`workspace task submit-result`-flow terug naar de ARCHITECT; alleen de OWNER kan
het exacte gecontroleerde resultaat aanvaarden. `executor status` en
`executor verify` schrijven niets en maken drift of een afgewerkte taak
zichtbaar.

## Veiligheid en beperkingen

- Lees `CONTEXT.md` altijd voordat u het deelt; geselecteerde broninhoud staat er
  letterlijk in.
- `.git/**`, `.opencntx/**`, `.env*`, `**/*.key` en `**/*.pem` zijn standaard
  uitgesloten, maar u blijft verantwoordelijk voor uw selectie.
- Alleen geldige UTF-8-tekst binnen de projectroot wordt ondersteund. Binaire
  bestanden, onleesbare bronnen, `..`-ontsnapping en symlink-ontsnapping worden
  geweigerd.
- Budgetoverschrijding is een fout; OPENCNTX kapt een pakket nooit stil af.
- `pack` en `verify` wijzigen geen bronbestanden.
- De gepubliceerde `v0.1.0`-tag bevat alleen de kern. De actuele
  `0.2.0.dev0`-bron voegt de lokale workspaceflow toe, maar is nog geen
  definitieve `v0.2.0`-release. Geen van beide doet AI-samenvatting,
  automatische bronselectie, PDF-/beeldextractie, agentstart, MCP, GUI, cloud,
  database of hosting.
- OPENCNTX is een lokaal hulpmiddel, geen garantie dat gedeelde context veilig,
  volledig of geschikt is voor een specifieke AI-tool.

Zie [SECURITY.md](SECURITY.md) voor het melden van kwetsbaarheden en aanvullende
privacywaarschuwingen. OPENCNTX is gelicentieerd onder Apache-2.0.
