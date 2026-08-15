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
- OPENCNTX 0.1 doet geen AI-samenvatting of automatische bronselectie en biedt
  geen PDF-/beeldextractie, agents, MCP, GUI, cloud, database of hosting.
- OPENCNTX is een lokaal hulpmiddel, geen garantie dat gedeelde context veilig,
  volledig of geschikt is voor een specifieke AI-tool.

Zie [SECURITY.md](SECURITY.md) voor het melden van kwetsbaarheden en aanvullende
privacywaarschuwingen. OPENCNTX is gelicentieerd onder Apache-2.0.
