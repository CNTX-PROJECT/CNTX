# Security in gewone taal

[Documentatie-index](README.md) · [Workspace](workspace.md) ·
[OWNER-flow](owner-flow.md)

Dit document is een leesbare samenvatting. De enige canonieke en volledige
securitypolicy is [SECURITY.md](../SECURITY.md). Bij verschil is die rootpolicy
altijd leidend.

## Lokale vertrouwensgrens

OPENCNTX werkt met bestanden die de lokale gebruiker aanwijst. De tool heeft
geen account, API-key, netwerkfunctie, cloudservice of ingebouwde AI. Dat maakt
de datastroom overzichtelijk, maar beschermt niet tegen iemand die al
schrijftoegang tot de projectmap heeft.

Hashes maken wijziging zichtbaar; ze voorkomen geen wijziging. Actornamen zoals
`OWNER`, `ARCHITECT` en `UITVOERDER-1` zijn lokale verklaringen, geen
cryptografisch bewijs van een natuurlijke persoon. Bescherm daarom de
projectmap met passende bestandsrechten en beperk schrijftoegang.

## Context kan gevoelige tekst bevatten

`CONTEXT.md` bevat geselecteerde broninhoud letterlijk. Lees het bestand altijd
voordat u het kopieert of aan een externe AI-tool geeft. Een lokaal gebouwd
pakket is geen toestemming om gegevens extern te verzenden.

OPENCNTX sluit standaard onder meer `.git/**`, `.opencntx/**`, `.env*`,
`**/*.key` en `**/*.pem` uit. Deze lijst vervangt geen eigen beoordeling.
Bewaar geen wachtwoorden, tokens, API-keys, persoonsgegevens of
productiegeheimen in een contextpakket of gedeelde werkruimte.

## Privacylabels zijn geen slot

`PUBLIC`, `PRIVATE`, `RESTRICTED` en `QUARANTINED` zijn lokale classificaties.
Ze bieden geen encryptie, authenticatie of toegangscontrole. `QUARANTINED`
wordt door contextselectie geweigerd en `RESTRICTED` vereist een expliciete
broninput, maar het bestandssysteem blijft de echte toegangspoort.

## Onvertrouwde inhoud blijft data

Bronnen, afgeleide tekst, hoofdstukken, context, playbooks, rollen, resultaten
en bewijs worden als lokale data behandeld. Instructies in die inhoud krijgen
geen OWNER-bevoegdheid en mogen de roadmap, taakgates of vaste verboden acties
niet opheffen.

OPENCNTX voert aangeleverde bestanden niet uit en start geen parser, OCR,
transcriptie, shell, netwerkverbinding, AI of agent. Een afzonderlijk extern
programma kan andere risico's hebben; beoordeel diens toegang, privacy,
netwerkgedrag en kosten apart.

## Fail-closed controles

De tool weigert onder andere:

- pad- of symlinkontsnapping buiten de bedoelde root;
- binaire of ongeldige UTF-8-input waar tekst vereist is;
- ontbrekende, gewijzigde of verkeerd gepinde bytes;
- budgetoverschrijding of stil afgekapt contextmateriaal;
- ongeldige eventketens en overgeslagen taakstatussen;
- stale hoofdstukken, bronnen, context, playbooks, rollen of uitvoerderrecords;
- taaksluiting zonder voorafgaande exacte OWNER-aanvaarding.

Een non-zero exitcode, `STALE`, `INVALID`, `BLOCKED` of andere foutstatus is een
stopteken. Corrigeer de oorzaak; negeer de controle niet en maak geen verborgen
retry.

## Verwijderen en provenance

`workspace media remove` is de enige gerichte verwijdering in deze laag. Het
vereist de exacte identifiers en digests en verwijdert alleen de genoemde
afgeleide `content.txt`. Origineel en andere afleidingen blijven bestaan; een
klein tombstonerecord bewaart provenance.

## Kwetsbaarheid melden

Meld een kwetsbaarheid niet in een openbaar issue. Gebruik **Report a
vulnerability** onder het tabblad **Security** van de GitHub-repository, zoals
beschreven in de canonieke [Security Policy](../SECURITY.md).
