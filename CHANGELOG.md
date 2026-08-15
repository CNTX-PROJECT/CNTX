# Changelog

Alle belangrijke wijzigingen aan OPENCNTX worden in dit bestand vastgelegd.

## 0.1.0 - 2026-08-16

Eerste publieke release van de lokale, providerneutrale OPENCNTX-flow.

### Toegevoegd

- `opencntx init` voor een klein leesbaar configuratiesjabloon zonder bestaand
  bestand te overschrijven.
- `opencntx pack` voor deterministische selectie en atomische publicatie van
  `CONTEXT.md` en `manifest.json`.
- `opencntx verify` voor afzonderlijke rapportage van ongewijzigde, gewijzigde,
  ontbrekende en onverwachte bronnen.
- Expliciete includes, required-paden, exclusions, bestandsbudget en bytebudget.
- Relatieve bronpaden, bytegroottes en SHA-256-hashes in het manifest.
- Standaarduitsluiting van Git-metadata, gegenereerde pakketten, `.env`-paden en
  gangbare sleutelbestanden.
- Blokkering van binaire of onleesbare input, path traversal en symlink-escape
  buiten de projectroot.
- Lokale tests op Windows en Ubuntu voor de volledige `init`-, `pack`- en
  `verify`-flow.

### Bekende beperkingen

- Alleen lokale UTF-8-tekstbestanden worden ondersteund.
- Geen PDF-, Office-, beeld- of binaire extractie.
- Geen automatische selectie, samenvatting, embeddings of ranking.
- Geen AI-provider, agent, MCP-server, GUI, cloudservice, database of hosting.
- De gebruiker moet het gegenereerde contextpakket controleren voordat het wordt
  gedeeld.
