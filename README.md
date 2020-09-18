# Hakusovellus

Yksinkertainen tietokannan metadatan hakusovellus lääketieteen tutkijoille.
Hakusovellukseen on tallennettu pitkän seurantatutkimuksen lomakkeiden tiedot,
mihin niiden data on tallennettu, missä muodossa ja muuttujien nimet.
Näin lomakkeiden ja datan yhteiskäyttö sujuu helpommin.

# Otteita hakusovelluksen käyttöohjeesta:

Tässä dokumentissa kuvataan HKA Datatietoja – hakusovelluksen käyttöä ja päivitystä. Ohje on jaettu kahteen osaan: 
käyttäjälle ja ylläpitäjälle. Käyttäjälle – osiossa kuvataan hakusovellukseen käyttöön liittyviä ohjeita ja virheiden 
ilmoittamisohjeita. Ylläpitäjälle – osiossa käydään läpi, miten uudesta lomakkeesta tai biologisesta näytteestä kirjoitetaan 
SPSS-kuvailutiedosto, miten kuvailutiedostot laitetaan SAS – ohjelman avulla hakutauluihin ja miten koko ohjelma päivitetään 
noudattamaan uusia tauluja. 

1. Käyttäjälle 

1.1 Ohjeita sovelluksen käyttöön 

Ohjelma sijaitsee ######. Lataa pakattu kansio HKA Datatietoja omalle koneellesi ja pura kansio (klikkaa hiiren oikeaa puolta ja klikkaa ”Extract all”). 
HKA Datatietoja kansiosta löytyy ohjelman pikakuvake HKA Datatietoja, jonka tyyppi on application (ohjelman tunnistaa kettu kuvakkeesta). 
Klikkaamalla kuvaketta ohjelma käynnistyy. Ohjelma toimii Windows ympäristössä. 

Ohjelma toimii parhaiten koko näytön kokoisena (tyylittelyn takia). Vasemmalla ruudussa näkyvät haku työkalut ja oikealla ruudussa haun tuloksen tulkintaan
liittyviä ohjeita. Hakutyökaluissa on ensin alasvetovalikot tiedoille, tutkimusalalle/näytteelle ja alaotsikolle (aihe). Valitse ensin mistä tiedoista olet
kiinnostunut: tallennetuista biologisista näytteistä, kyselylomakkeista vai tutkimustiedoista. Tutkimustiedot kertovat, mitä tietoja kustakin tutkimusyksilöstä
on tallennettu. Tämän jälkeen valitse lomakkeiden kysymysten tutkimusala, biologisten näytteiden näyte tai tutkimustiedot joko lomakkeista tai biologisista näytteistä. 
Kyselylomakkeille voi valita myös aiheen, joka kaventaa valittua tutkimusalaa (katso dokumentti Questionaires HKA:n verkkosivuilta: 
https://www.utu.fi/fi/sivustot/cyri/tutkimustoiminta/hyvankasvunavaimet/Sivut/home.aspx). Lomakkeilla tutkimusalan valitseminen on pakollinen,
mutta tarkentavaa aihetta ei ole pakko määrittää. Vetolaatikoiden alla ovat valintalaatikot (tutkittavat), joiden avulla voi määrittää minkä tutkittavan
(lapsi, äiti tai puoliso) kysymykset, näytteet tai tiedot hakuun haluaa sisällyttää. Valinnalla tutkimustiedot – lomakkeet valintalaatikot eivät ole käytössä, 
koska data ei ole eritelty tutkittavien mukaan. Tämän jälkeen ohjelma tulostaa haun tulokset näytölle haku-painiketta klikkaamalla. 

Lomakkeiden tulostaulukko koostuu 15 sarakkeesta, joiden selitykset näkyvät taulukossa 1. Biologisten näytteiden tulostaulukko koostuu 11 sarakkeesta, joiden 
selitykset näkyvät taulukossa 2. (Taulukoita ei github.) Tutkimustietojen tulostaulukko biologisten näytteiden osalta koostuu HKA -id numerosta,
tutkimuskäynneistä ja näytteistä. Osaan näytteisiin on tarkennettu näytteen ottohetki lapsen ikänä. Lomakkeiden osalta tulostaulukko koostuu 
HKA – id numerosta ja lomakkeiden nimistä. Taulukoissa 1 tarkoittaa, että näyte on otettu kyseiseltä yksilöltä (lomakkeilla: yksilö on vastannut kyseiseen lomakkeeseen). 
0 tarkoittaa, että näytettä ei ole otettu (lomakkeilla: yksilö ei ole vastannut kyseiseen lomakkeeseen).   

Uuden haun voi tehdä sulkematta ohjelmaa välissä. Ohjelma ilmoittaa, jos hakuyhdistelmä ei toimi tai jos yhdistelmällä ei ole tulostaulukkoa. 

