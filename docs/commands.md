# Commandoreferentie

[Documentatie-index](README.md) · [Kern](core.md) · [Workspace](workspace.md) ·
[OWNER-flow](owner-flow.md)

Deze compacte index bevat exact 41 gedocumenteerde CLI-paden: 37 uitvoerbare
leaf-commando's en vier echte help-/oriëntatiepaden. De vier help-paden voeren
geen producthandeling uit; ze tonen de actuele parserstructuur. Gebruik bij een
uitvoercommando altijd `--help` voor de exacte argumenten en herhaalbare opties.

| Nr. | CLI-pad | Functie |
|---:|---|---|
| 1 | `opencntx --help` | toon de drie kerncommando's en workspace-ingang |
| 2 | `opencntx workspace --help` | toon de workspacegroepen en directe opdrachten |
| 3 | `opencntx workspace media --help` | toon de veilige media-afleidingsopdrachten |
| 4 | `opencntx workspace task --help` | toon de volledige lokale taakstatusmachine |
| 5 | `opencntx init` | maak veilig `opencntx.toml` in de huidige map |
| 6 | `opencntx pack` | bouw atomair `CONTEXT.md` en `manifest.json` |
| 7 | `opencntx verify` | controleer pakket, manifest en gepinde bronbytes |
| 8 | `opencntx workspace init` | maak de vaste lokale projectwerkruimte |
| 9 | `opencntx workspace capture` | registreer één regulier bestand byte-exact |
| 10 | `opencntx workspace chapter create` | maak één nieuw DRAFT-hoofdstuk met bronpins |
| 11 | `opencntx workspace catalog rebuild` | herbouw index en SQLite-catalogus uit officiële bestanden |
| 12 | `opencntx workspace media register` | registreer reeds aangeleverde UTF-8-afleiding |
| 13 | `opencntx workspace media review` | bind reviewbeslissing aan de exacte teksthash |
| 14 | `opencntx workspace media promote` | capture een REVIEWED afleiding bewust als tekstbron |
| 15 | `opencntx workspace media status` | toon afleidingsstatus zonder te schrijven |
| 16 | `opencntx workspace media verify` | controleer bron-, record-, review- en tekstbinding |
| 17 | `opencntx workspace media remove` | verwijder alleen exact gepinde afgeleide tekstbytes |
| 18 | `opencntx workspace playbook register` | registreer één onveranderlijke PROPOSED playbookrevisie |
| 19 | `opencntx workspace playbook approve` | keur exact één playbookdefinitie afzonderlijk goed |
| 20 | `opencntx workspace playbook status` | toon playbookstatus zonder wijziging |
| 21 | `opencntx workspace playbook verify` | controleer revisie, definitie en approvalrecord |
| 22 | `opencntx workspace role register` | registreer één begrensde PROPOSED rolrevisie |
| 23 | `opencntx workspace role approve` | keur exact één roldefinitie afzonderlijk goed |
| 24 | `opencntx workspace role status` | toon rolstatus zonder wijziging |
| 25 | `opencntx workspace role verify` | controleer revisie, grenzen en approvalrecord |
| 26 | `opencntx workspace executor prepare` | bind taak, context, playbook en rol in één pakket |
| 27 | `opencntx workspace executor status` | toon actuele of afgewerkte uitvoerderstatus |
| 28 | `opencntx workspace executor verify` | controleer het volledige uitvoerderrecord read-only |
| 29 | `opencntx workspace context build` | bouw deterministisch één taakgebonden contextpakket |
| 30 | `opencntx workspace context verify` | controleer de levende taak- en contextbinding read-only |
| 31 | `opencntx workspace task propose` | leg doel, inputs, grenzen en acceptatie vast |
| 32 | `opencntx workspace task approve` | bind OWNER-goedkeuring aan revisie en proposal-digest |
| 33 | `opencntx workspace task begin` | registreer de overgang naar `IN_EXECUTION` |
| 34 | `opencntx workspace task submit-result` | bewaar exact één resultaat en optioneel bewijs |
| 35 | `opencntx workspace task review-result` | bind ARCHITECT-review aan het exacte resultaat |
| 36 | `opencntx workspace task accept-result` | registreer OWNER-besluit over resultaat en review |
| 37 | `opencntx workspace task close` | sluit alleen na een geldig OWNER-`ACCEPT` |
| 38 | `opencntx workspace task status` | valideer en toon de volledige append-only taakketen |
| 39 | `opencntx workspace task record-attempt` | registreer foutsignatuur voor de anti-deadloopgate |
| 40 | `opencntx workspace task cancel` | beëindig de taak expliciet als geannuleerd |
| 41 | `opencntx workspace task supersede` | beëindig de taak ten gunste van een benoemde opvolger |

## Exacte opties vinden

Voeg `--help` toe aan het volledige uitvoerpad:

```powershell
opencntx verify --help
opencntx workspace capture --help
opencntx workspace context build --help
opencntx workspace executor prepare --help
opencntx workspace task accept-result --help
```

Deze referentie is een navigatiekaart en verandert de CLI niet. Een woord in
een gids is nooit een nieuw commando of een bevoegdheid om een taak, merge,
release, publicatie, AI of extern proces te starten.
