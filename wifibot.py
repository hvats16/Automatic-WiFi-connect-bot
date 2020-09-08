import os 
import sys


saved_networks = os.popen("netsh wlan show profiles").read()
print(saved_networks)

avaible_network = os.popen("netsh wlan show networks").read()
print(avaible_network)

preferred_network = input("Enter the preferred WiFi for your connection: ")

response = os.popen("netsh wlan disconnect").read()
print(response)

if preferred_network not in saved_networks:
    print(preferred_network+" network is not saved in system")
    print("Your connection can't establish")
    sys.exit()
else:
    print(preferred_network+" network saved in our system")
    

while True:
    avail = os.popen("netsh wlan show networks").read()
    if preferred_network in avail:
        print("Network Found")
        break

print("Connecting......")
resp = os.popen("netsh wlan connect name =" +" " + preferred_network + ' ').read()
print(resp)
