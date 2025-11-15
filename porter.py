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
parser.add_argument("target",help="Type the target IP adress")
args = parser.parse_args() #read user argumentss

#open json 
with open("ports.json", "r") as f:
 data =json.load(f) 

openPorts=[]
print(f"Searching for open ports in {args.target}...") 

def Scan1000_CommonPorts():
 for x in data["common_ports"]:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket per port
  sock.settimeout(3)
  result = sock.connect_ex(((args.target) , int(x)))
  if result == 0:
   openPorts.append(x) 
  sock.close()
 #RESULTS
print(f"Scan ended, open ports : {len(openPorts)} ")
for p in openPorts:
 print(f"{p} ---> OPEN")

#Verify if the host is UP before scanning target
host = args.target
response = ping(host)
if not response:
 print("Unable to ping the host; it may be offline.")
else:
  print("Host is up.")
  Scan1000_CommonPorts()

 
 
 
   








