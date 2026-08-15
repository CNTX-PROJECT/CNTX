# OPENCNTX

OPENCNTX maakt een klein, expliciet en controleerbaar contextpakket voor één AI-taak. De tool blijft lokaal en roept geen AI-provider aan.

Deze eerste projectstap levert alleen een veilige `init`-flow. `pack` en `verify` volgen in de volgende roadmapopdracht.

## Starten

Vereist: Python 3.11 of nieuwer.

```powershell
python -m pip install -e .
python -m opencntx init
```

`init` maakt `opencntx.toml` in de huidige projectmap en overschrijft nooit een bestaand bestand.

Bekijk de beschikbare opdracht:

```powershell
python -m opencntx --help
```

## Huidige grens

- lokaal en providerneutraal;
- geen netwerk, account, API-key of database;
- nog geen contextpakketgeneratie of verificatie;
- gelicentieerd onder Apache-2.0.
