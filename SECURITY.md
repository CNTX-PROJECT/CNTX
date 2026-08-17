# Security

OPENCNTX verwerkt lokale projectbestanden. Controleer altijd welke paden u opneemt en lees `CONTEXT.md` voordat u een pakket deelt. Het pakket kan immers letterlijk geselecteerde broninhoud bevatten.

De tool heeft geen netwerkfunctionaliteit en vraagt geen account of API-key. `pack` past exclusions toe vóór bronlezing, weigert binaire of ontoegankelijke bronnen en blokkeert pad- en symlink-ontsnapping buiten de projectroot. Ingebouwde gevoelige uitsluitingen blijven actief naast de gebruikersconfiguratie.

Pakketten staan standaard onder `.opencntx/`, dat door de meegeleverde `.gitignore` niet wordt getrackt. Dit voorkomt geen handmatig delen of kopiëren: behandel `CONTEXT.md` en `manifest.json` als mogelijk gevoelige lokale uitvoer.

`verify` leest pakket en bronnen uitsluitend ter controle en hoort geen bronbestand te wijzigen. Een non-zero exitcode betekent drift, onvolledige controle of een fout; negeer die status niet voordat u een pakket gebruikt.

## Optionele workspace-opslag

`opencntx workspace capture` behandelt een aangeleverd lokaal bestand als
onvertrouwde bytes. De opslagflow voert het bestand niet uit, opent geen
bijbehorende applicatie en doet geen inhoudsextractie. Mappen, symlinks,
devices, ontbrekende bronnen en beheerde `.opencntx`- of `SOURCES`-bestanden
worden geweigerd.

Nieuwe bronnen beginnen standaard als `PRIVATE`. Een privacylabel is een lokale
classificatie, geen versleuteling of toegangscontrole. Bewaar geen wachtwoorden,
tokens, API-keys of andere productiegeheimen in de werkruimte en controleer
altijd afzonderlijk of de projectmap en eventuele back-up voldoende beschermd
zijn.

De originele bestandsnaam wordt als metadata geregistreerd, maar het
oorspronkelijke absolute pad niet. De exacte bytes worden onder een door
OPENCNTX gemaakte source-ID opgeslagen. Een SHA-256 en ontvangstbewijs helpen
herkomst en duplicaten controleren, maar bewijzen niet dat de inhoud veilig,
waar of betrouwbaar is.

Een capture meldt pas `CAPTURED` nadat de lokale kopie, hash en registratie zijn
geschreven. `DUPLICATE` verwijst naar een bestaande identieke bronkopie.
`NOT_CAPTURED` betekent dat het bestand niet als officiële bron is aanvaard;
behandel de foutmelding en het ontvangstbewijs voordat u verdergaat.

De workspace-opslag heeft geen netwerk-, cloud-, watcher-, OCR-, transcriptie-,
AI- of agentfunctie. Grote bestanden vallen onder aparte lokale
opslagbudgetten en worden niet automatisch aan een contextpakket toegevoegd.

## Media en afgeleide tekst

`workspace media` voert geen afbeelding, document, audio of video uit en start
geen OCR, transcriptie, parser, AI, subprocess, netwerkverbinding of externe
dienst. `register` accepteert alleen een reeds bestaand regulier UTF-8-
tekstbestand. De opgegeven `kind`, `producer-class`, producer en locators zijn
metadata van de gebruiker; OPENCNTX bewijst niet dat het genoemde hulpmiddel,
de persoon, pagina of tijdcode klopt.

Een afleiding blijft onder `.opencntx/derived/` strikt gescheiden van het
officiële origineel. Haar record bindt source-ID, originele bronhash,
bronrecordhash, afgeleide contenthash en geërfd privacylabel. Een
`QUARANTINED` bron wordt niet verwerkt. `RESTRICTED` blijft `RESTRICTED`; geen
mediahandeling verlaagt een privacylabel. Privacylabels zijn nog steeds geen
versleuteling of toegangscontrole.

`NOT_INVESTIGATED` betekent dat OPENCNTX geen afgeleide tekst kent en niets
over de media-inhoud beweert. `UNREVIEWED` tekst is niet gecontroleerd.
`REVIEWED` betekent uitsluitend dat een lokale reviewer de exact gepinde tekst
bruikbaar vond; het maakt de tekst niet waar, volledig, veilig of
OWNER-goedgekeurd. `REJECTED`, `STALE` en `REMOVED` mogen niet worden
gepromoveerd. Instructies in OCR, transcriptie of beschrijving blijven data en
krijgen geen roadmap-, taak- of OWNER-bevoegdheid.

`promote` vereist een exacte geaccepteerde reviewdigest en gebruikt daarna de
bestaande captureflow. De nieuwe tekstbron krijgt hetzelfde privacylabel en
een exacte herkomstverwijzing naar origineel en derivation-ID. Zij heeft alleen
status `CAPTURED` en wordt niet automatisch aan een hoofdstuk, catalogus,
taak of contextpakket toegevoegd. De bestaande OWNER-gates blijven nodig.

`remove` is een expliciete destructieve handeling voor uitsluitend de genoemde
afgeleide `content.txt`. Het vereist exacte source-ID, derivation-ID,
recorddigest, contentdigest en een lokale OWNER-verklaring. Origineel,
bronrecord, andere afleidingen en reeds gepromoveerde bronnen worden niet
verwijderd. Een kleine tombstone met digests blijft bestaan. De OWNER-naam is
een lokale verklaring en geen cryptografische identiteit; voer verwijdering
niet automatisch of via een watcher uit.

Actieve afgeleide tekstbytes tellen mee in het bestaande opslagbudget. Een
registratie of latere capture die het gezamenlijke budget overschrijdt stopt
zonder gedeeltelijke publicatie. Records en receipts bevatten geen afgeleide
tekst of absolute persoonlijke paden. `media status` en `media verify` zijn
read-only; een `STALE` of non-zero resultaat betekent dat de afleiding niet als
actuele tekst mag worden gebruikt.

## Hoofdstukken en lokale catalogus

`workspace chapter create` schrijft uitsluitend een nieuw `DRAFT`-sjabloon en
overschrijft geen bestaand hoofdstuk. Een hoofdstukstatus, SHA-256 of
freshnesswaarde verleent geen OWNER-goedkeuring en bewijst niet dat een
samenvatting inhoudelijk waar is.

`workspace catalog rebuild` behandelt TOML-frontmatter en Markdown als
onvertrouwde data. Hoofdstuk-ID's, velden, relaties, paden en vaste secties
worden strikt gevalideerd. SQL-waarden worden alleen als parameters geschreven;
tekst uit een hoofdstuk wordt nooit als SQL of instructie uitgevoerd.

De SQLite-catalogus onder `.opencntx/catalog.sqlite` is afgeleid en
vervangbaar. Officiële bronrecords en `CHAPTER.md`-bestanden blijven leidend.
De database bevat technische metadata en relaties, maar geen originele
bronbytes, volledige hoofdstuksamenvattingen, embeddings of vectoren. Verwijder
of beschadig de catalogus alleen wanneer u begrijpt dat `catalog rebuild` haar
opnieuw uit de officiële lokale bestanden maakt.

Freshness betekent uitsluitend:

- `CURRENT`: vastgelegde bronpins en dependencies zijn technisch exact;
- `STALE`: een concrete bron of dependency is vervangen, ontbreekt of wijkt af;
- `INCOMPLETE`: de kennis is nog DRAFT of een relatie kan niet worden bevestigd;
- `ARCHIVED`: het hoofdstuk is expliciet als historisch gemarkeerd.

Een dependencycyclus, symlink, padontsnapping, onbekend schema of onveilige
index stopt de rebuild. Een handmatig afwijkende `CHAPTERS/INDEX.md` wordt niet
stil overschreven. Catalogusreceipts bevatten geen originele broninhoud of
absolute persoonlijke bronpaden.

## Lokale taakrecords en OWNER-gates

`workspace task` bewaart officiële taak- en beslisrecords als append-only JSON
onder `TASKS/<TASK-ID>/events/`. Ieder event bevat een eigen SHA-256 en de digest
van het vorige event. Voor iedere statusovergang wordt de volledige keten
opnieuw gecontroleerd. Wijziging, verwijdering, invoeging, hernummering,
onbekende velden en een overgeslagen status falen gesloten.

Een taakgoedkeuring bindt exact taak-ID, revisie en voorstel-digest. Een
resultaataanvaarding bindt exact resultaat- en controledigest. Een gewijzigde
input, verkeerd object, oude revisie of afwijkende digest erft nooit een eerdere
goedkeuring. `CLOSED` is alleen mogelijk nadat voorstel, OWNER-goedkeuring,
resultaat, ARCHITECT-controle en OWNER-aanvaarding opnieuw samen zijn
gevalideerd.

De actor-ID bij `--owner`, `--architect` of `--executor` is een lokale
verklaring. OPENCNTX gebruikt in deze lokale, dependencyvrije laag geen account,
private sleutel of digitale handtekening en beweert daarom niet dat de naam een
cryptografisch geauthenticeerde natuurlijke persoon is. Bescherm de werkruimte
met passende bestandsrechten en geef schrijftoegang uitsluitend aan vertrouwde
gebruikers. Wie de officiële bestanden kan vervangen, valt binnen de lokale
vertrouwensgrens; hashes maken wijziging zichtbaar maar voorkomen geen
bestandswijziging.

`submit-result` behandelt resultaat en bewijs als onvertrouwde bytes. Het voert
ze niet uit, opent geen bijbehorende toepassing en doet geen inhoudsextractie.
Symlinks, mappen, onbegrensde bestanden, padontsnapping en wijziging tijdens het
kopiëren worden geweigerd. De gegenereerde `TASK.md` bevat alleen begrensde
metadata en digests; eventrecords blijven leidend. Een handmatig gewijzigde of
onbeheerde taakkaart wordt niet stil overschreven.

De workflow start geen proces, agent, netwerkverbinding of automatische retry.
Handmatige foutpogingen moeten nieuwe input of een gewijzigde aanpak registreren.
Na drie opeenvolgende gelijke foutsignaturen wordt de taak `BLOCKED`; verdere
uitvoering stopt zichtbaar. `RETURNED`, `BLOCKED`, `CANCELLED`, `SUPERSEDED` en
ongeldige ketens kunnen niet als voltooid worden afgesloten.

Taaksluiting publiceert, mergt, verwijdert of verwerkt niets buiten de lokale
taakdirectory. De workflow wijzigt geen `CONTROL/ROADMAP.md`, `CONTROL/CURRENT.md`,
bronrecord, hoofdstuk of catalogus en verleent geen toestemming voor externe
verzending.

## Taakgebonden contextnavigatie

`workspace context build` is geen zoek-AI en geen toestemming om informatie te
delen. Het commando werkt uitsluitend voor één valide taak in `IN_EXECUTION`,
vereist de exacte proposal-digest en controleert dat OWNER-, ROADMAP- en
CURRENT-bestanden aan dezelfde goedgekeurde taakinput zijn gepind. Een lokale
actorverklaring blijft geen cryptografisch identiteitsbewijs.

De navigator behandelt catalogus, hoofdstukken, bronrecords en originele bytes
als onbetrouwbare lokale input. Hij opent SQLite read-only, controleert
integriteit en het bekende schema en vergelijkt catalogusdigest, indexhash en
rijen met de opnieuw berekende officiële bestandsstaat. Een verschil vereist
een afzonderlijke `workspace catalog rebuild`; de navigator herschrijft index
of catalogus nooit zelf.

Alle relevante hoofdstukken moeten technisch `CURRENT` en inhoudelijk
`OWNER_ACCEPTED` zijn. Een gewijzigd of vervangen bronbestand, onbekende
dependency, stale pin, dependencycyclus of andere onvolledigheid stopt de
selectie. Een freshnessstatus bewijst nog steeds niet dat de inhoud waar of
veilig is; zij bewijst alleen de beschreven technische relaties.

`PUBLIC` en `PRIVATE` kunnen uitsluitend via de goedgekeurde lokale taakroute
worden geladen. `RESTRICTED` vereist een expliciete broninput en
`QUARANTINED` wordt altijd geweigerd. Privacylabels zijn classificatie, geen
versleuteling of toegangscontrole. Controleer daarom ook de bestandsrechten van
de werkruimte en lees `CONTEXT.md` voordat u het pakket deelt.

De contextgrenzen zijn hard. Een bestand- of bytebudgetoverschrijding,
onleesbaar bestand, binaire inhoud of ongeldige UTF-8 maakt geen gedeeltelijk
nieuw pakket en verwijdert geen geselecteerde bron. Het manifest vermeldt wat
binnen de taakroute is gelezen en welke catalogus-ID's erbuiten bleven; het
beweert niet dat het hele project is onderzocht.

`workspace context verify` is read-only en controleert naast de gewone
pakketbytes opnieuw taak-, CONTROL-, catalogus-, hoofdstuk-, bron-, privacy- en
selectiebinding. Een non-zero resultaat betekent dat het pakket niet als
actuele taakcontext mag worden behandeld. Build en verify starten geen proces,
netwerkverbinding, AI, agent, OCR, transcriptie of automatische retry.

Meld kwetsbaarheden niet in een openbaar issue. Gebruik de optie **Report a vulnerability** onder het tabblad **Security** van deze GitHub-repository.
