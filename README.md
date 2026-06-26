# Dronepohjainen 360 videoratkaisu

## Equipment
* [DJI Mavic Pro](https://www.dji.com/fi/support/product/mavic)
* [Arduino Nano](https://store.arduino.cc/products/arduino-nano)
* 250mL syringe
* Steel compression spring
* 5-6V DC Peristatic pump
* UART Transciever modules 2X
* [Motor driver circuit](https://github.com/LaplandUAS/Verijalki/tree/main/pcb)
* [3D printed parts and accessories](https://github.com/LaplandUAS/Verijalki/tree/main/cad)

## Mechatronics
The demonstrator's mechatronics consist of a drone-mounted liquid payload dispenser, which is built of a spring loaded 250mL syringe, terminated with a peristatic pump for flow control. The syringe stays pressurised under the compression spring, and a peristatic pump is both used as a valve, and a method to mitigate clogs caused by blood coagulation and the low viscosity of anti-caking and anti-coagulation additives in low temperatures. The compression spring inhibits air from being pulled back into the payload.

## Electronics
The pump's flow rate is controlled wirelessly utilizing a pair of [HC-12](https://www.allaboutcircuits.com/projects/understanding-and-implementing-the-hc-12-wireless-transceiver-module/) Transciever modules. Any other UART-based transcievers that operate in a completely transparent mode can be used without extra configuration. The transmitter's signal is decoded from serial by an Atmega168 microcontroller onboard the motor driver, which translates the signal to match the pump's flow rate issued by the transmitter via an H-bridge IC. The transmitter device consists of an Arduino Nano, a control potentiometer, a matching HC-12 transciever and a battery pack. The motor controller is also capable of transmitting a callback signal indicating the payload depletion once an embedded magnet in the syringe trips a reed-switch placed at the level of depletion on the syringe body.

Either a separate battery pack, or an USB breakout board can be used to power the control circuit on board the drone. The Mavic Pro's add-on port uses a basic micro-USB connector in the following pin configuration:
| Micro-USB Pin  | Label |
| ------------- |:-------------:|
| 1      | GND  |
| 2      | 5V   |
| 3      | 1.5V |
| 4      |?     |
| 5      |?     |

> [!CAUTION]
> The DJI Mavic pro doesn't follow any USB standard for it's add-on port. Use third party devices on this port at your own risk!

Only pins `1 & 2` are necessary for this application.

-----
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="/img/logot/license.png">
  <source media="(prefers-color-scheme: light)" srcset="/img/logot/license_lightmode.png">
  <img alt="License logo" src="/img/logot/license.png">
</picture>
