# Workspace en bronnen

[Documentatie-index](README.md) · [OWNER-flow](owner-flow.md) ·
[Commandoreferentie](commands.md) · [Security](security.md)

De optionele workspace-laag zit in de ontwikkelbron `0.2.0.dev0`. Zij ordent
lokale projectinformatie zonder een bestand uit te voeren of inhoud als waar
te aanvaarden.

## Werkruimte maken

```powershell
opencntx workspace init mijn-project
```

De opdracht maakt leesbare mappen voor besturing, inbox, bronnen,
hoofdstukken, taken, playbooks en rollen. Een bestaande complete werkruimte
wordt niet herschreven. Een gedeeltelijke of conflicterende structuur wordt
geweigerd.

## Eén bron vastleggen

```powershell
opencntx workspace capture plan.pdf --root mijn-project --origin OWNER
```

`capture` accepteert precies één regulier lokaal bestand en:

- bewaart de exacte bytes onder een unieke source-ID;
- registreert grootte, SHA-256, UTC-tijd, herkomst en privacylabel;
- gebruikt standaard privacy `PRIVATE`;
- herkent een exact duplicaat zonder een tweede bronkopie;
- opent, verplaatst, verwijdert of voert het aangeleverde bestand niet uit;
- schrijft een klein ontvangstbewijs onder `.opencntx/receipts/`.

De zichtbare eindstatus is `CAPTURED`, `DUPLICATE` of `NOT_CAPTURED`.
Privacylabels zijn `PUBLIC`, `PRIVATE`, `RESTRICTED` en `QUARANTINED`. Met
`--supersedes SOURCE-ID` verwijst een nieuwe inhoudsversie expliciet naar een
oudere bron. Een label is classificatie, geen encryptie of toegangscontrole.

## Hoofdstuk maken

```powershell
opencntx workspace chapter create CH-ELEKTRICITEIT `
  --title "Elektriciteit" `
  --source SRC-20260816-0123456789ab `
  --root mijn-project
```

`chapter create` schrijft uitsluitend een nieuw
`CHAPTERS/CH-ELEKTRICITEIT/CHAPTER.md`-sjabloon als `DRAFT`. Iedere herhaalde
`--source` legt de actuele geregistreerde bron-SHA-256 vast. Herhaalde
`--depends-on`-opties leggen hoofdstukafhankelijkheden vast.

Een DRAFT, digest of technische freshnessstatus is geen inhoudelijke
OWNER-goedkeuring. Een bestaand hoofdstuk wordt niet overschreven.

## Catalogus herbouwen

```powershell
opencntx workspace catalog rebuild --root mijn-project
```

De herbouw:

- leest officiële bronrecords en `CHAPTER.md`-bestanden;
- hercontroleert bronbytes, pins en afhankelijkheden;
- berekent `CURRENT`, `STALE`, `INCOMPLETE` of `ARCHIVED`;
- regenereert `CHAPTERS/INDEX.md`;
- vervangt `.opencntx/catalog.sqlite` pas na integriteitscontrole;
- toont dezelfde state-digest in index en catalogus.

Markdownbronnen en hoofdstukken blijven officieel. De SQLite-catalogus en
index zijn afgeleid en volledig herbouwbaar. Een dependencycyclus, onbekend
schema, onveilig pad of gewijzigde beheerde index stopt gesloten.

## Media en afgeleide UTF-8-tekst

`capture` kan media byte-exact bewaren, maar OPENCNTX voert geen OCR,
transcriptie, parser, beeld- of videoanalyse uit. Alleen reeds aangeleverde
UTF-8-tekst kan als afleiding worden geregistreerd:

```powershell
opencntx workspace media register SRC-... `
  --text afgeleid.txt `
  --kind OCR `
  --producer-class LOCAL_TOOL `
  --producer "offline-tool 1" `
  --locator "pagina 1-3" `
  --root mijn-project
```

De afleiding blijft gescheiden onder `.opencntx/derived/` en bindt aan de
exacte originele bronbytes en het geërfde privacylabel. De maker- en
locatormetadata zijn lokale verklaringen, geen door OPENCNTX bewezen feiten.

Mogelijke statussen:

- `NOT_INVESTIGATED`: geen afleiding bekend;
- `UNREVIEWED`: geregistreerd maar niet menselijk gecontroleerd;
- `REVIEWED`: exact gepinde tekst bruikbaar bevonden, niet automatisch waar;
- `REJECTED`: afgewezen en niet promoveerbaar;
- `PROMOTED`: bewust via de gewone captureflow als tekstbron opgeslagen;
- `STALE`: bron-, record- of tekstbytes wijken af;
- `REMOVED`: tekstkopie verwijderd, provenance bewaard.

`media review` bindt een beslissing aan de exacte contentdigest. Alleen
`REVIEWED` kan met de getoonde reviewdigest via `media promote` een gewone
`CAPTURED` tekstbron worden. Die bron wordt niet automatisch een feit,
hoofdstuk, taakinput of contextbestand.

`media remove` verwijdert alleen de exact geïdentificeerde afgeleide
`content.txt` na controle van source-ID, derivation-ID, recorddigest,
contentdigest en een lokale OWNER-verklaring. Origineel, andere afleidingen en
reeds gepromoveerde bronnen blijven bestaan; een tombstone bewaart provenance.

Gebruik [de commandoreferentie](commands.md) en de betreffende `--help`-route
voor alle verplichte opties. Lees voor taakselectie en contextbouw verder in
[OWNER-flow en taakgates](owner-flow.md).
