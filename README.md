# OPENCNTX

OPENCNTX maakt een klein, expliciet en controleerbaar contextpakket voor één AI-taak. De tool werkt volledig lokaal en roept geen AI-provider aan.

## Starten

Vereist: Python 3.11 of nieuwer.

```powershell
python -m pip install -e .
python -m opencntx init
python -m opencntx pack
python -m opencntx verify .opencntx/latest
```

`init` maakt `opencntx.toml` in de huidige projectmap en overschrijft nooit een bestaand bestand.

Vul daarin één doel, inclusies, verplichte bestanden, uitsluitingen en twee budgetten in. `pack` maakt daarna atomair exact twee primaire bestanden:

- `.opencntx/latest/CONTEXT.md` — direct bruikbare context in Markdown;
- `.opencntx/latest/manifest.json` — relatieve bronpaden, bytes, SHA-256-hashes, selectie en uitsluitredenen.

`verify` vergelijkt het pakket later met de actuele bronnen en toont `unchanged`, `changed`, `missing` en `unexpected` afzonderlijk. Exitcode `0` betekent gelijk; `1` betekent drift of een onvolledige controle; `2` betekent een configuratie- of uitvoerfout.

Bekijk de beschikbare opdracht:

```powershell
python -m opencntx --help
```

## Veiligheidsgrens

- lokaal en providerneutraal;
- geen netwerk, account, API-key of database;
- alleen geldige UTF-8-tekst binnen de projectroot;
- binaire en ontoegankelijke bronnen worden geweigerd;
- symlink- en `..`-ontsnapping buiten de projectroot wordt geblokkeerd;
- `.git/**`, `.opencntx/**`, `.env*`, `**/*.key` en `**/*.pem` blijven standaard uitgesloten;
- budgetoverschrijding levert een fout op en nooit een stil afgekapt pakket;
- bronbestanden worden door `pack` en `verify` nooit gewijzigd;
- gelicentieerd onder Apache-2.0.
