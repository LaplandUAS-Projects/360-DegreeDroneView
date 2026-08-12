# GoPro 360° Street View -aineiston muodostustyökalu

Tämä projekti automatisoi GoPro 360° -kameralla kuvatun videomateriaalin käsittelyn Street View -tyyppiseksi selaimessa tarkasteltavaksi aineistoksi. Ratkaisu muodostaa videosta tasavälein otettuja kuvia, yhdistää niihin GPS-sijainnit ja laskee kulkusuunnan (yaw) kuvien välisen navigoinnin mahdollistamiseksi.

Järjestelmä on suunniteltu erityisesti dronekuvauksessa tuotetun 360°-materiaalin käsittelyyn ja julkaisemiseen verkkoselaimessa käytettäväksi katselunäkymäksi.

## Kuvausprosessi

1. Varmista, että GoPro-kameran GPS-toiminto on käytössä.
   - Dronen GPS-dataa ei käytetä tässä prosessissa.
   - Kaikki paikannustieto luetaan GoPro-videon sisältämästä telemetriadatasta.

2. Suorita kuvaus droneen kiinnitetyllä 360°-kameralla.

3. Siirrä kuvausmateriaali tietokoneelle.

4. Muunna GoPron alkuperäinen videotiedosto MP4-muotoon GoPro Player -ohjelmistolla.

5. Pura GPS-data videosta GoPro Telemetry Extractor -työkalulla.

6. Suorita tämän projektin automaatiotyökalu:
   - poimii videosta kuvat valitulla aikavälillä
   - synkronoi GPS-tiedot kuviin
   - laskee kulkusuunnan (yaw)
   - muodostaa selaimessa käytettävän aineiston

7. Julkaise tuotettu lopputulos verkkosivustolle tai avaa paikallisesti selaimessa.

## Vaadittava laitteisto

- Drone
- GoPro 360° -kamera
- Tietokone videonkäsittelyä varten

> [!NOTE]
> GoPro 360° -kameran paino ja ilmanvastus lisäävät dronen kuormitusta. Varmista, että käytettävä drone kykenee kantamaan kameran turvallisesti.

## Vaadittava ohjelmisto

### Pakolliset

- Python 3
- FFmpeg
- GoPro Player
- GoPro Telemetry Extractor

### Ulkoiset työkalut

- GoPro Player
- https://goprotelemetryextractor.com/free/

> [!NOTE]
> GoPro Player ja GoPro Telemetry Extractor ovat maksuttomia käyttää, mutta Telemetry Extractor -palvelu vaatii rekisteröitymisen.

## Suositeltu laitteisto

Videon muuntaminen GoPron alkuperäisestä formaatista MP4/HEVC-muotoon on laskennallisesti raskas operaatio. Suorituskykyinen prosessori ja mahdollinen laitteistokiihdytys (GPU) nopeuttavat käsittelyä merkittävästi.

## Projektin toimintaperiaate# Dronepohjainen 360 videoratkaisu
Dronepohjainen 360 asteen videoratkaisu on esimerkki siitä, miten olemassa olevaa kuvaus- ja paikkatietoteknologiaa voidaan yhdistää uudenlaisen, immersiivisen käyttäjäkokemuksen tuottamiseksi. Toteutettiin Google Street View -tyylinen liikuttava näkymä hyödyntäen dronekuvausta ja 360° videotekniikkaa. Ratkaisussa käyttäjä voi tarkastella ympäristöä vapaasti ja edetä kuvattua reittiä pitkin saumattomasti. 

## Laitteisto
* [DJI Mavic Pro](https://www.dji.com/fi/support/product/mavic)
* [3D printed parts and accessories](https://github.com/LaplandUAS-Projects/360-DegreeDroneView/tree/main/cad)

-----
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/img/logot/license.png">
  <source media="(prefers-color-scheme: light)" srcset="/img/logot/license_lightmode.png">
  <img alt="License logo" src="/img/logot/license.png">
</picture>
