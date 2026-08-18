# OPENCNTX-documentatie

[Terug naar de publieke landingspagina](../README.md)

Gebruik de kortste route die bij uw vraag past:

- [Kern: init, pack en verify](core.md) — maak één klein contextpakket en
  controleer later of de bronbytes nog exact gelijk zijn.
- [Workspace en bronnen](workspace.md) — bewaar aangeleverde bestanden, orden
  hoofdstukken, herbouw de catalogus en registreer afgeleide tekst veilig.
- [OWNER-flow en taakgates](owner-flow.md) — verdeel één taak, bind context en
  sluit alleen na afzonderlijke OWNER-aanvaarding.
- [Commandoreferentie](commands.md) — vind alle 37 uitvoercommando's en vier
  echte help-/oriëntatiepaden.
- [Security in gewone taal](security.md) — begrijp de lokale vertrouwensgrens,
  privacylabels en fail-closed bescherming.
- [Platformen en controles](platforms.md) — zie ondersteunde Pythonversies,
  handmatige platformbewijzen en de huidige CI-status.

## Snelle keuze

| Ik wil… | Lees eerst |
|---|---|
| drie lokale tekstcommando's gebruiken | [Kern](core.md) |
| een projectwerkruimte en bronnen ordenen | [Workspace](workspace.md) |
| OWNER-goedkeuringen en taken begrijpen | [OWNER-flow](owner-flow.md) |
| een exact CLI-pad vinden | [Commando's](commands.md) |
| weten wat hashes en labels wel of niet bewijzen | [Security](security.md) |
| Windows-, Ubuntu-, Python- of CI-status controleren | [Platformen](platforms.md) |

## Productgrens

OPENCNTX maakt lokale, expliciete en verifieerbare contextpakketten. De
workspace-laag ordent lokale bronnen en bewijsrecords. OPENCNTX start geen AI,
agent, proces, OCR, transcriptie, cloudservice of netwerkverbinding.

De CLI-help blijft de exacte bron voor opties en verplichte argumenten:

```powershell
opencntx --help
opencntx workspace --help
opencntx workspace task --help
```

Voor kwetsbaarheidsmeldingen en de volledige beveiligingsgrenzen geldt alleen
de canonieke [Security Policy](../SECURITY.md).
