# Degrade_AP

Degrade_AP is a Scapy based script meant to disrupt communications of an Access Point (AP) and any clients trying to 
interact with that AP for a designated period of time

## Dependencies
To ensure scapy is installed, run the following
````
$ sudo pip3 install -r requirements.txt
OR
$ sudo pip3 install scapy
````

## Running
Degrade_AP needs to be ran as superuser or as a sudo privileged user
due to the commands (ifconfig and iwconfig) being run within the script.
````
sudo python3 degrade_ap.py
````

## Adjustable Constants

#### INTERVAL
Interval is an integer value that denotes time in seconds. The default is set to 120,
meaning that Degrade_AP will shoot de-authentication frames for two minutes and 
will rest for two minutes until aborted

#### REASON
Reason is an integer value that denotes the reason code attached to the de-authentication frame.
https://www.cisco.com/assets/sol/sb/WAP371_Emulators/WAP371_Emulator_v1-0-1-5/help/Apx_ReasonCodes2.html

## Notes
Future iterations plan to use argparser for passing parameters