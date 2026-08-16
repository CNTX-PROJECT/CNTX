# OPENCNTX

OPENCNTX maakt voor één AI-taak een klein, expliciet en controleerbaar
contextpakket. U kiest zelf de lokale tekstbronnen; OPENCNTX bundelt ze met
paden, groottes en SHA-256-hashes. De tool werkt zonder account, netwerk, API-key
of AI-provider.

## Installeren

Vereist: Python 3.11 of nieuwer en Git voor onderstaande download. Versie 0.1
staat niet op PyPI; de GitHub-bronrelease gebruikt de standaard
Python-packageflow:

```powershell
git clone --branch v0.1.0 --depth 1 https://github.com/CNTX-PROJECT/OPENCNTX.git
cd OPENCNTX
python -m pip install .
```

Controleer daarna met `opencntx --help` of de installatie beschikbaar is.

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

> Dit onderdeel is ontwikkelwerk na de gepubliceerde `v0.1.0` en maakt geen
> deel uit van de installatie vanaf die tag zolang geen latere release is
> goedgekeurd.

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

De leesbare frontmatter van `CONTROL/CURRENT.md` legt standaard maximaal 2 GiB
per bron en 20 GiB officiële bronopslag vast. Deze opslagbudgetten staan los
van de veel kleinere contextbudgetten van `pack`.

Deze lokale werkruimtelaag doet bewust geen achtergrondbewaking, chatopname,
netwerkdownload, cloudback-up, OCR, transcriptie, beeld- of videoanalyse,
vrije zoekopdracht, AI-selectie of agentuitvoering. De SQLite-catalogus is
uitsluitend een lokale, herbouwbare metadata-index.

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
- De gepubliceerde OPENCNTX 0.1-tag doet geen AI-samenvatting of automatische
  bronselectie en biedt geen PDF-/beeldextractie, agents, MCP, GUI, cloud,
  database of hosting. De latere workspace-ontwikkeling blijft lokaal en is
  niet automatisch onderdeel van die tag of release.
- OPENCNTX is een lokaal hulpmiddel, geen garantie dat gedeelde context veilig,
  volledig of geschikt is voor een specifieke AI-tool.

Zie [SECURITY.md](SECURITY.md) voor het melden van kwetsbaarheden en aanvullende
privacywaarschuwingen. OPENCNTX is gelicentieerd onder Apache-2.0.
