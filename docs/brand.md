# OPENCNTX-huisstijl

[Documentatie-index](README.md) · [Publieke landingspagina](../README.md)

De officiële vorm is een achtzijdige grens rond een centraal contextnetwerk.
De grens staat voor een expliciet contextpakket; de ruit, verbindingen en vier
knooppunten staan voor bewust geselecteerde relaties. Het merk gebruikt geen
brein, robot, chatballon of ander algemeen AI-symbool.

## Woordmerk

- `OPEN` is altijd paars.
- `CNTX` is bijna-zwart op een lichte achtergrond.
- `CNTX` is wit op een donkere achtergrond.
- Gebruik exact `OPENCNTX`, in hoofdletters en zonder spatie.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../assets/brand/opencntx-wordmark-dark.svg">
  <img src="../assets/brand/opencntx-wordmark-light.svg" width="640" alt="OPENCNTX-woordmerk">
</picture>

## Kleuren en contrast

| Rol | Licht | Donker |
|---|---|---|
| Achtergrond | `#F7F5FB` | `#0B0B0F` |
| Structuur en `CNTX` | `#0B0B0F` | `#FFFFFF` |
| Grafisch paars | `#7C3AED` | `#A855F7` |
| Paars voor `OPEN` | `#6D28D9` | `#C084FC` |

De tekstparen halen minimaal WCAG AA: bijna-zwart/licht 18,16:1,
donkerpaars/licht 6,57:1, wit/donker 19,64:1 en lichtpaars/donker 7,43:1.
Grafische accenten halen minimaal 3:1 tegen hun bedoelde achtergrond.

## Officiële bestanden

- [Licht symbool](../assets/brand/opencntx-symbol-light.svg)
- [Donker symbool](../assets/brand/opencntx-symbol-dark.svg)
- [Licht woordmerk](../assets/brand/opencntx-wordmark-light.svg)
- [Donker woordmerk](../assets/brand/opencntx-wordmark-dark.svg)
- [Avatarbron](../assets/brand/opencntx-avatar.svg)
- [Social-previewbron](../assets/brand/opencntx-social-preview.svg)
- [Avatar-PNG 512×512](../assets/brand/opencntx-avatar-512.png)
- [Social-preview-PNG 1280×640](../assets/brand/opencntx-social-preview-1280x640.png)
- [Icoon-PNG 32×32](../assets/brand/opencntx-icon-32.png)
- [Icoon-PNG 128×128](../assets/brand/opencntx-icon-128.png)
- [SHA-256-manifest](../assets/brand/SHA256SUMS)

De zes SVG's zijn de officiële vectorbronnen. De vier PNG's zijn gecontroleerde
afleidingen en nooit de bron van waarheid. Alle lettervormen bestaan uit native
SVG-geometrie; er is geen fontdownload, rastertekst, script of externe asset.

## Ruimte en minimumgrootte

- Houd rond symbool en woordmerk minimaal één knooppuntdiameter vrije ruimte.
- Gebruik het losse symbool niet kleiner dan 32×32 pixels.
- Gebruik het horizontale woordmerk niet smaller dan 240 pixels.
- Kies altijd de lichte of donkere variant die bij de achtergrond hoort.

## Niet doen

- verander de verhouding, volgorde, letterkleuren of geometrie niet;
- voeg geen verloop, schaduw, gloed, textuur of animatie toe;
- plaats geen tekst of decoratie binnen de vrije ruimte;
- maak van een PNG geen nieuwe vectorbron;
- gebruik de lichte variant niet op donker of de donkere variant niet op licht.

## Reproduceren en controleren

De renderer gebruikt alleen de Python-standaardbibliotheek en schrijft
deterministische RGBA-PNG's met vaste chunks en bytes:

```powershell
python tools/render_brand.py --check
```

`--check` rendert tijdelijk opnieuw en vergelijkt alle afleidingen en
`SHA256SUMS` byte-exact. Gebruik `--write` uitsluitend na een bewust beoordeelde
wijziging aan een officiële SVG-bron.

Voor vragen of bijdragen gelden [SUPPORT.md](../SUPPORT.md) en
[CONTRIBUTING.md](../CONTRIBUTING.md). Meld een kwetsbaarheid uitsluitend via
de route in [SECURITY.md](../SECURITY.md).
