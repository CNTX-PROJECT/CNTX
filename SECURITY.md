# Security

OPENCNTX verwerkt lokale projectbestanden. Controleer altijd welke paden u opneemt en lees `CONTEXT.md` voordat u een pakket deelt. Het pakket kan immers letterlijk geselecteerde broninhoud bevatten.

De tool heeft geen netwerkfunctionaliteit en vraagt geen account of API-key. `pack` past exclusions toe vóór bronlezing, weigert binaire of ontoegankelijke bronnen en blokkeert pad- en symlink-ontsnapping buiten de projectroot. Ingebouwde gevoelige uitsluitingen blijven actief naast de gebruikersconfiguratie.

Pakketten staan standaard onder `.opencntx/`, dat door de meegeleverde `.gitignore` niet wordt getrackt. Dit voorkomt geen handmatig delen of kopiëren: behandel `CONTEXT.md` en `manifest.json` als mogelijk gevoelige lokale uitvoer.

`verify` leest pakket en bronnen uitsluitend ter controle en hoort geen bronbestand te wijzigen. Een non-zero exitcode betekent drift, onvolledige controle of een fout; negeer die status niet voordat u een pakket gebruikt.

Meld kwetsbaarheden niet in een openbaar issue. Gebruik de optie **Report a vulnerability** onder het tabblad **Security** van deze GitHub-repository.
