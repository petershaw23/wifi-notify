# wichtig: mit "sudo python3 wifind.py" starten, sonst findet er keine MAC adressen
import os
import nmap

target_mac = "B0:2A:43:FC:19:2F"
print("Target Mac: " + target_mac)

nm = nmap.PortScanner()
nm.scan(hosts='192.168.0.0/24', arguments='-sP')

host_list = nm.all_hosts()
print(host_list)
for host in host_list:
    if 'mac' in nm[host]['addresses']:
        print(host+' : '+nm[host]['addresses']['mac'])
        if target_mac == nm[host]['addresses']['mac']:
            print('Target Found')
