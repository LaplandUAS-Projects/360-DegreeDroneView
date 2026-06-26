# Dronepohjainen 360 videoratkaisu
Dronepohjainen 360 asteen videoratkaisu on esimerkki siitä, miten olemassa olevaa kuvaus- ja paikkatietoteknologiaa voidaan yhdistää uudenlaisen, immersiivisen käyttäjäkokemuksen tuottamiseksi. Toteutettiin Google Street View -tyylinen liikuttava näkymä hyödyntäen dronekuvausta ja 360° videotekniikkaa. Ratkaisussa käyttäjä voi tarkastella ympäristöä vapaasti ja edetä kuvattua reittiä pitkin saumattomasti. 

## Laitteisto
* [DJI Mavic Pro](https://www.dji.com/fi/support/product/mavic)
* [Arduino Nano](https://store.arduino.cc/products/arduino-nano)
* 250mL syringe
* Steel compression spring
* 5-6V DC Peristatic pump
* UART Transciever modules 2X
* [Motor driver circuit](https://github.com/LaplandUAS/Verijalki/tree/main/pcb)
* [3D printed parts and accessories](https://github.com/LaplandUAS/Verijalki/tree/main/cad)

## Mekaniikka
Selitä mekaniikka

## Elektroniikka
Selitä elektroniikka. Esimerkki linkeistä --->  [HC-12](https://www.allaboutcircuits.com/projects/understanding-and-implementing-the-hc-12-wireless-transceiver-module/) 

Esimerkki kytkennöistä
| Micro-USB Pin  | Label |
| ------------- |:-------------:|
| 1      | GND  |
| 2      | 5V   |
| 3      | 1.5V |
| 4      |?     |
| 5      |?     |

esimerkki varoituksesta
> [!CAUTION]
> The DJI Mavic pro doesn't follow any USB standard for it's add-on port. Use third party devices on this port at your own risk!

esimerkki korostuksesta
Only pins `1 & 2` are necessary for this application.

-----
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/img/logot/license.png">
  <source media="(prefers-color-scheme: light)" srcset="/img/logot/license_lightmode.png">
  <img alt="License logo" src="/img/logot/license.png">
</picture>
