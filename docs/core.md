# Kern: init, pack en verify

[Documentatie-index](README.md) · [Commandoreferentie](commands.md) ·
[Security](security.md)

De kern maakt voor één taak een begrensd pakket van lokale UTF-8-tekst. De
gebruiker kiest de bronnen; OPENCNTX selecteert niet semantisch en vat niets
samen.

## 1. Configuratie maken

Ga naar de lokale projectroot en voer uit:

```powershell
opencntx init
```

Dit maakt `opencntx.toml` en overschrijft nooit een bestaand bestand. Een klein
voorbeeld:

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

De velden betekenen:

- `goal`: het ene doel waarvoor het pakket wordt gemaakt;
- `include`: expliciete relatieve bestanden of globpatronen;
- `required`: paden die aanwezig en geselecteerd moeten zijn;
- `exclude`: extra uitsluitingen bovenop de ingebouwde veilige uitsluitingen;
- `max_files`: harde bovengrens voor het aantal geselecteerde bestanden;
- `max_bytes`: harde bovengrens voor hun gezamenlijke bytes.

Ingebouwde uitsluitingen, waaronder `.git/**`, `.opencntx/**`, `.env*`,
`**/*.key` en `**/*.pem`, blijven actief. Budgetoverschrijding is een fout; de
tool kapt nooit stil bestanden of bytes af.

## 2. Pakket maken

```powershell
opencntx pack
```

Een geslaagde run publiceert atomair precies twee primaire bestanden onder
`.opencntx/latest/`:

- `CONTEXT.md` met het doel, begrenzing en de letterlijke geselecteerde tekst;
- `manifest.json` met relatieve paden, groottes, SHA-256-hashes, selectie en
  uitsluitredenen.

Een bestaand compleet pakket blijft intact als de nieuwe bouw faalt. De tool
leest geen bron buiten de projectroot, volgt geen onveilige symlink en weigert
binaire, onleesbare of ongeldige UTF-8-input.

## 3. Pakket controleren

```powershell
opencntx verify .opencntx/latest
```

`verify` vergelijkt pakket, manifest en actuele bronbytes en rapporteert:

- `unchanged`: bron bestaat en digest is gelijk;
- `changed`: bron bestaat maar bytes of digest wijken af;
- `missing`: gepinde bron bestaat niet meer;
- `unexpected`: pakket bevat iets dat niet door het manifest wordt verwacht.

De controle is read-only en herbouwt het pakket niet.

## Exitcodes

| Code | Betekenis |
|---|---|
| `0` | opdracht geslaagd of controle exact gelijk |
| `1` | drift of een onvolledige verificatie |
| `2` | configuratie-, validatie- of uitvoerfout |

Een non-zero code mag niet worden genegeerd voordat het pakket wordt gebruikt
of gedeeld.

## Wat de kern niet doet

De kern doet geen AI-selectie, samenvatting, ranking, embeddings, OCR,
PDF-/beeldextractie, netwerkdownload, cloudopslag, agentstart, GUI of MCP. Een
geldig pakket bewijst welke bytes werden opgenomen; het bewijst niet dat de
inhoud waar, volledig of veilig voor een externe AI-tool is.

Lees daarom altijd `CONTEXT.md` zelf voordat u het buiten uw lokale project
gebruikt.
