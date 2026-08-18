# Platformen en controles

[Documentatie-index](README.md) · [Kern](core.md) ·
[Commandoreferentie](commands.md)

## Ondersteunde Pythonversies

De package-metadata ondersteunt Python 3.11, 3.12 en 3.13. De runtime heeft
geen dependencies buiten de Python-standaardbibliotheek.

Andere Pythonversies worden niet door deze documentatie als ondersteund
geclaimd.

## Bewezen platformen

De volledige suite is handmatig uitgevoerd op:

- Windows met Python 3.13;
- Ubuntu met Python 3.12.

Bij de laatste geïntegreerde basis waren 128 van 128 tests op beide routes
groen, met `PYTHONDONTWRITEBYTECODE=1` en `ResourceWarning` als fout. De 8B-
kandidaat moet na toevoeging van zes kwaliteitscontroles exact 134 van 134
tests op beide platformen halen voordat een Draft PR aan de OWNER wordt
voorgelegd.

Dit bewijs claimt niet dat ieder ander besturingssysteem of iedere mogelijke
Python-/shellcombinatie praktisch is getest.

## Handmatig testen

PowerShell:

```powershell
$env:PYTHONDONTWRITEBYTECODE = "1"
python -W error::ResourceWarning -m unittest discover -s tests
python -m pip wheel . --no-deps --wheel-dir dist
```

Ubuntu-shell:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 -W error::ResourceWarning -m unittest discover -s tests
python3 -m pip wheel . --no-deps --wheel-dir dist
```

Wheelinstallatie en `opencntx --help` moeten daarna vanuit een tijdelijke
testlocatie worden gecontroleerd. Gegenereerde wheels, caches en
installatie-uitvoer horen niet in Git.

## Voorbereide CI-matrix

De repository bevat een begrensde workflowdefinitie voor exact zes combinaties:

| Runner | Python |
|---|---|
| `ubuntu-latest` | 3.11, 3.12 en 3.13 |
| `windows-latest` | 3.11, 3.12 en 3.13 |

Iedere combinatie is ontworpen om:

1. de volledige testsuite met ResourceWarnings als fout uit te voeren;
2. één wheel zonder runtime-dependencies te bouwen;
3. exact dat wheel te installeren;
4. package- en metadataversie te vergelijken;
5. `opencntx --help` als geïnstalleerde CLI-smoke uit te voeren.

De workflow heeft uitsluitend `contents: read`, bewaart geen checkout-
credentials, gebruikt geen secrets en publiceert niets. Officiële Actions zijn
op volledige immutable commits vastgepind.

## Huidige CI-status

De live GitHub-repository-instelling heeft Actions nog uitgeschakeld. Daarom is
de juiste status:

`CI_DEFINED_INACTIVE`

De workflow is gedefinieerd, maar kan nog geen live run of check produceren.
Nul workflowruns of nul checks is nadrukkelijk geen groen CI-bewijs. Tot een
afzonderlijk goedgekeurde GitHub-instelling de workflow activeert, blijven
Windows- en Ubuntu-controles handmatig verplicht.

Activatie, branch protection en required checks vallen buiten deze
documentatieopdracht.
