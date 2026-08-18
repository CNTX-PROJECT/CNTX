# Changelog

Alle belangrijke wijzigingen aan OPENCNTX worden in dit bestand vastgelegd.

## Unreleased - doelversie 0.2.0

Deze wijzigingen staan op de ontwikkelbranch en zijn nog niet als `v0.2.0`
gepubliceerd.

### Toegevoegd

- Een lokaal workspace-opslagfundament dat aangeleverde bestanden byte-exact
  registreert met privacylabel, herkomst, SHA-256 en ontvangstbewijs.
- Onveranderlijke hoofdstukrevisies en een volledig herbouwbare lokale
  catalogus voor bronnen, afhankelijkheden, freshness en CURRENT-status.
- Append-only taakrecords met afzonderlijke exacte OWNER-goedkeuring voor
  voorstel en resultaat, sluiting pas na aanvaarding, en een begrensde
  anti-deadloopstop.
- Een deterministische taakgebonden contextnavigator die uitsluitend expliciet
  gepinde CONTROL-, taak-, hoofdstuk-, playbook-, rol- en bronrelaties volgt.
- Veilige registratie, review, promotie en verwijdering van reeds aangeleverde
  afgeleide UTF-8-tekst, zonder zelf OCR, transcriptie of AI uit te voeren.
- Voorgestelde en exact goedgekeurde playbooks en rollen, met maximaal één
  lokaal uitvoerderpakket dat geen mens, proces, tool, AI of agent start.
- Uitbreiding van de publieke suite naar 128 tests, inclusief één controle die
  package- en Pythonversie exact gelijk houdt.
- Een compacte publieke documentatiestructuur met één index en taakgerichte
  gidsen voor kern, workspace, OWNER-flow, commando's, security en platformen.
- Zes dependencyvrije regressietests voor lokale documentlinks, structuur en
  het begrensde CI-beleid; de publieke suite telt daardoor 134 tests.
- Een read-only cross-platform CI-definitie voor Windows en Ubuntu met Python
  3.11, 3.12 en 3.13, vastgepinde officiële Actions, wheelbouw en CLI-smoke.

### Gevalideerd

- De volledige suite slaagt op Windows/Python 3.13 en Ubuntu/Python 3.12 met
  ResourceWarnings als fouten.
- Een private praktijktest bevestigde dat de taakcontext klein, vindbaar,
  herleidbaar en bruikbaar blijft en dat een fout fail-closed zonder retry of
  gedeeltelijke uitvoering stopt.

### Bekende beperkingen

- `0.2.0.dev0` is ontwikkelcode en nog geen gepubliceerde `v0.2.0`-release.
- OPENCNTX doet geen AI-aanroep, automatische samenvatting, OCR, transcriptie,
  embeddings, vector search, kennisgraaf, agentstart of procesuitvoering.
- Er is geen cloudservice, externe database, watcher, GUI, MCP of PyPI-release.
- Levende taakcontext wordt gecontroleerd terwijl de taak `IN_EXECUTION` is;
  na taaksluiting vormen de append-only taakketen, digests, resultaat, bewijs en
  uitvoerderstatus het historische afrondingsbewijs.
- GitHub Actions staat nog uit. De workflow is daarom voorbereid maar blijft
  `CI_DEFINED_INACTIVE` totdat een afzonderlijk goedgekeurde GitHub-instelling
  haar activeert; nul workflowruns zijn geen groen CI-bewijs.

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
