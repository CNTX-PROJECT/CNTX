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

Meld kwetsbaarheden niet in een openbaar issue. Gebruik de optie **Report a vulnerability** onder het tabblad **Security** van deze GitHub-repository.
