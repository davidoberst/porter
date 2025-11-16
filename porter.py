import socket
import pyfiglet
import argparse
import json
import time
from ping3 import ping

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
sock.settimeout(1)

#pyfiglet text
print(pyfiglet.figlet_format("Porter", font="small"))
time.sleep(1)
#Add parameters
parser = argparse.ArgumentParser()
parser.add_argument("target",help="Type the target IP adress") #IP ARGUMENT

parser.add_argument("-p",help="Comma-separated list of ports to scan (example: 80,443,8080)",required=False) #PORT ARGUMENT

args = parser.parse_args() #read user argumentss

#open json 
with open("ports.json", "r") as f:
 data =json.load(f) 

openPorts=[]


def Scan1000_CommonPorts(): #SCAN DEFAULT PORTS
    print(f"Searching for open ports in {args.target}...") 
    for x in data["common_ports"]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((args.target, int(x)))
        if result == 0:
            openPorts.append(x)
        sock.close()
   
    print(f"Scan ended, open ports : {len(openPorts)} ")
    for p in openPorts:
        print(f"{p} ---> OPEN")


def ScanGivenPorts(target, port_list): #SCAN GIVEN PORTS (-p)
    print(f"Searching for open ports ({args.p}) in {args.target}...")
    ports = port_list.split(",")  
    for z in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result = sock.connect_ex((target, int(z)))
        if result == 0:
            openPorts.append(z)
        sock.close()

    print(f"Scan ended, open ports : {len(openPorts)}")
    for p in openPorts:
        print(f"{p} ---> OPEN")
      
#Verify if the host is UP before scanning target
host = args.target
response = ping(host)
if response is None:
 print("Unable to ping the host; it may be offline.")
 exit()

print("Host is up.")
  
if args.p:
 ScanGivenPorts(args.target,args.p)  
else:
   Scan1000_CommonPorts()

 
 
 
   








