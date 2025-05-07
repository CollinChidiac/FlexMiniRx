# FlexMiniRx
A script to serve Unifi FlexMini Recovery firwmare
![flex](https://github.com/user-attachments/assets/689fc590-5c3a-43ca-a7e4-317e9e7a1b2c)

I know that others may find the instructions from Unifi daunting or convoluted so I made this to help simplify the process.

Requirements:
Windows
Python 3.x

How to use the script:

1. Select the network adapter you are using with the dropdown
2. Select "Set Static IP"
3. Download and install the latest version of Python 3.x (ENSURE TO SELECT 'Add Python to PATH" DURING INSTALL)
https://www.python.org/downloads/
4. Select Verify Python Installation, if python is found continue, if not reinstall python
5. Select "Create Webserver Directory"
6. Select Download Firmware, download the latest version of the USW-Flex-Mini Firmware
https://ui.com/download/software/usw-flex-mini
7. Select your firmware file that you just downloaded using 6
8. Start the Web Server


Now lets work on that Flex-Mini:
1. Unplug everything from the Flex-mini
2. Plug your windows machine directly into the Flex-mini
3. Ensure that the Flex power is off (no PoE, no USB)
4. Press and hold down the reset button on the bottom of the Flex
5. While still hodling down the reset button, plug it back into power
6. Keep holding the reset button until the LED has gone through a Blue > White > Off status


Offical Unifi documentation:
https://help.ui.com/hc/en-us/articles/360043360253-UniFi-Recovery-Mode
