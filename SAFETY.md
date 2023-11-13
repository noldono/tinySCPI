# Safety Disclaimer
Our team had the original intent of creating a safety measure which detects signals outside of the tinySA's specification, and halt operations when necessary. This, however, proved to not only impact user performance, but became a concern with user rights. Therefore, we dropped this feature early in development.

By using this library, the user acknowledges the possibility and safety concerns of [human exposure to RF](https://www.fcc.gov/general/radio-frequency-safety-0).
This software comes with no warranty and the user is responsible to his or her own safety when utilizing our library. The user agrees that tinySCPI team is not responsible for any damages caused by the operation of the tinySA through this software.

## Input
The tinySA supports an absolute maximum input level without attenuation of +10dBm (0.01W). Any higher powered signals may cause harm to the device, and to the user. 

## Output
The tinySA can act as a low powered transmitter. However, modifying the device or attaching a high gain antenna to output at a higher level may cause harmful interference. By using this software, the user agrees to abide by all applicable regulations regarding unlicensed, licensed, intentional, and/or unintentional transmission of RF signals.

As mentioned in the [tinySA wiki](https://tinysa.org/wiki/pmwiki.php?n=Main.Transmitters), the best approach is to use ALWAYS a 30dB attenuator directly connected to the tinySA and to use power attenuators to reduce the output of the transmitter to the target input level of this 30dB attenuator, that is +10dBm 

Additionally, it is always recommended to output at the lowest available level. 

### Resources

[Information regarding FCC regulations for low-power, non-licensed transmission](https://www.fcc.gov/media/radio/low-power-radio-general-information)

[RF Devices](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-15?toc=1)

[ARRL Graphical Frequency Allocations](http://www.arrl.org/graphical-frequency-allocations)

[RF Safety FAQ](https://www.fcc.gov/engineering-technology/electromagnetic-compatibility-division/radio-frequency-safety/faq/rf-safety)

[Radio Frequency Interference Best Practices Guidebook](https://www.cisa.gov/sites/default/files/publications/safecom-ncswic_rf_interference_best_practices_guidebook_2.7.20_-_final_508c.pdf)