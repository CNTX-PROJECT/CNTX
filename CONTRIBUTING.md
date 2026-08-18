# Bijdragen aan OPENCNTX

Dank u dat u OPENCNTX wilt verbeteren. Houd een bijdrage klein, controleerbaar
en gericht op één duidelijk probleem.

## Voor u begint

1. Lees de [publieke documentatie](docs/README.md) en zoek bestaande issues.
2. Gebruik [SUPPORT.md](SUPPORT.md) voor vragen en installatiehulp.
3. Meld een mogelijke kwetsbaarheid nooit openbaar; volg [SECURITY.md](SECURITY.md).
4. Open voor grotere wijzigingen eerst een functieverzoek. Een voorstel of PR
   is geen automatische toezegging of goedkeuring.

## Lokale controle

OPENCNTX vereist Python 3.11 of nieuwer en heeft geen runtime-dependencies.

```powershell
python -W error::ResourceWarning -m unittest discover -s tests
python -m pip wheel . --no-deps --wheel-dir dist
```

Voor wijzigingen aan de huisstijl:

```powershell
python tools/render_brand.py --check
```

Wijzig gegenereerde PNG-bestanden en `assets/brand/SHA256SUMS` niet handmatig.
Pas eerst de officiële SVG-bron aan en regenereer daarna bewust de afleidingen.

## Grenzen voor een pull request

- Eén doel en een zo klein mogelijke diff.
- Geen geheimen, tokens, persoonsgegevens of private projectinhoud.
- Geen nieuwe dependency zonder een afzonderlijk gemotiveerd besluit.
- Geen product-, security- of authoritybelofte die de bestaande documentatie
  tegenspreekt.
- Voeg tests en documentatie toe wanneer gedrag of publieke uitleg verandert.
- Bevestig welke controles werkelijk zijn uitgevoerd; nul checks is geen groen
  bewijs.

Door bij te dragen stemt u ermee in dat uw bijdrage onder de bestaande
[Apache-2.0-licentie](LICENSE) wordt verspreid.
