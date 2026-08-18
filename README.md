# OPENCNTX

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/opencntx-wordmark-dark.svg">
  <img src="assets/brand/opencntx-wordmark-light.svg" width="640" alt="OPENCNTX — OPEN in paars, CNTX in zwart of wit">
</picture>

OPENCNTX maakt voor één AI-taak een klein, expliciet en controleerbaar
contextpakket. U kiest zelf de lokale tekstbronnen; OPENCNTX bundelt ze met
paden, groottes en SHA-256-hashes. De tool werkt lokaal, zonder account,
API-key, netwerkfunctie of verplichte AI-provider.

OPENCNTX kan daarnaast een lokale projectwerkruimte ordenen met bronnen,
hoofdstukken, taken, afzonderlijke OWNER-goedkeuringen en begrensde
uitvoerderpakketten. Het start zelf geen AI, agent, proces, OCR of transcriptie.

## Versiestatus

| Versie | Inhoud | Status |
|---|---|---|
| `v0.1.0` | `init`, `pack` en `verify` | Gepubliceerde kernrelease |
| `0.2.0.dev0` op `main` | Kern plus lokale `workspace`-flow | Ontwikkelversie; nog geen `v0.2.0`-release |

OPENCNTX staat niet op PyPI. Python 3.11 of nieuwer is vereist.

## Installeren

Gepubliceerde kernrelease `v0.1.0`:

```powershell
git clone --branch v0.1.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

Actuele ontwikkelbron `0.2.0.dev0`, inclusief `workspace`:

```powershell
git clone --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

Controleer de installatie met:

```powershell
opencntx --help
```

## Kern in drie commando's

Ga naar de lokale projectmap en maak de configuratie:

```powershell
opencntx init
```

Vul in `opencntx.toml` één doel en de toegestane bronnen in:

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

Maak en controleer daarna het contextpakket:

```powershell
opencntx pack
opencntx verify .opencntx/latest
```

`pack` schrijft `CONTEXT.md` en `manifest.json` onder `.opencntx/latest/`.
Lees `CONTEXT.md` altijd zelf voordat u het aan een AI-tool geeft. `verify`
meldt gewijzigde, ontbrekende en onverwachte bronnen afzonderlijk.

Lees de volledige kernuitleg in [Kern: init, pack en verify](docs/core.md).

## Lokale projectwerkruimte

De ontwikkelversie kan aangeleverde bestanden byte-exact bewaren en ordenen:

```powershell
opencntx workspace init mijn-project
opencntx workspace control refresh --root mijn-project
opencntx workspace capture plan.pdf --root mijn-project --origin OWNER
```

De workspace kan daarna onder meer:

- bronnen registreren zonder ze uit te voeren;
- hoofdstukken en een herbouwbare lokale catalogus beheren;
- reeds aangeleverde afgeleide UTF-8-tekst veilig registreren;
- taken als append-only keten met afzonderlijke OWNER-gates vastleggen;
- een kleine actuele roadmapsturing automatisch als control-snapshot afleiden;
- voor één goedgekeurde taak een klein deterministisch contextpakket bouwen;
- goedgekeurde playbooks en rollen aan één begrensd uitvoerderpakket binden.

Privacylabels zijn classificatie, geen encryptie of toegangscontrole. Een
digest maakt wijziging zichtbaar, maar bewijst niet dat inhoud waar of veilig
is. Bij een exact gemarkeerd actueel roadmapblock gebruikt contextbouw
automatisch een compacte afgeleide snapshot; de volledige roadmap blijft op
SHA-256 gepind. Lees [Workspace en bronnen](docs/workspace.md) voor de flow.

## OWNER-flow

De bedoelde volgorde is:

```text
OWNER-doel
→ ARCHITECT-analyse en voorstel
→ exacte OWNER-goedkeuring
→ begrensde uitvoering
→ ARCHITECT-review
→ exacte OWNER-aanvaarding
→ sluiting met bewijs
```

Levende pakket- en contextverificatie gebeurt terwijl de taak nog
`IN_EXECUTION` is en vóór resultaatindiening. Na taaksluiting worden de
append-only taakketen, gepinde digests, resultaat, bewijs en uitvoerderstatus
als historisch bewijs gecontroleerd.

Lees de volledige volgorde in [OWNER-flow en taakgates](docs/owner-flow.md).

## Documentatie

- [Documentatie-index](docs/README.md) — kies de kortste leesroute.
- [Kern: init, pack en verify](docs/core.md) — configuratie, uitvoer en
  exitcodes.
- [Workspace en bronnen](docs/workspace.md) — opslag, hoofdstukken, catalogus
  en media-afleidingen.
- [OWNER-flow en taakgates](docs/owner-flow.md) — taak, context, playbook, rol
  en uitvoerderpakket.
- [Commandoreferentie](docs/commands.md) — de bestaande commandokaart plus de
  compacte control-refresh.
- [Security in gewone taal](docs/security.md) — lokale vertrouwensgrens en
  veilige omgang met context.
- [Platformen en controles](docs/platforms.md) — Python-, Windows-, Ubuntu- en
  CI-status.
- [Huisstijl](docs/brand.md) — officiële logo's, kleuren en gebruiksregels.

## Veiligheidsgrenzen

- `.git/**`, `.opencntx/**`, `.env*`, `**/*.key` en `**/*.pem` worden standaard
  uitgesloten. Compacte taakcontext maakt alleen voor de beheerde
  `.opencntx/control-snapshot.md` een expliciete uitzondering.
- Kernpakketten ondersteunen alleen geldige lokale UTF-8-tekst binnen de
  projectroot; binaire input en pad- of symlinkontsnapping worden geweigerd.
- Budgetoverschrijding kapt nooit stil context af.
- Een control-snapshot is afgeleid, herschrijft de roadmap niet en verleent
  nooit OWNER-bevoegdheid.
- Bron-, context-, playbook-, rol- en resultaatinhoud blijft data en krijgt
  nooit automatisch OWNER-bevoegdheid.
- OPENCNTX start geen AI, agent, shell, externe dienst of netwerkverbinding.
- OPENCNTX garandeert niet dat gedeelde context volledig, waar of veilig is.

Lees de canonieke [Security Policy](SECURITY.md) voordat u gevoelige informatie
verwerkt. Meld kwetsbaarheden via **Report a vulnerability** op GitHub, niet via
een openbaar issue.

## Projectstatus

De bron op `main` is `0.2.0.dev0` en nog niet uitgebracht als `v0.2.0`.
De voorbereide GitHub Actions-workflow is `CI_DEFINED_INACTIVE` zolang Actions
voor het repository uit staat. Nul workflowruns zijn geen groen CI-bewijs;
Windows- en Ubuntu-controles blijven tot activatie handmatig verplicht.

Zie [CHANGELOG.md](CHANGELOG.md) voor wijzigingen. OPENCNTX is gelicentieerd
onder [Apache-2.0](LICENSE).
