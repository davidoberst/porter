import socket
import pyfiglet
import argparse
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
sock.settimeout(1)

print(pyfiglet.figlet_format("Porter", font="small"))
time.sleep(1)

#Add parameters
parser = argparse.ArgumentParser()
parser.add_argument("target",help="Type the target IP adress")
parser.add_argument("port",help="Target Port")
args = parser.parse_args() #read user argumentss

print(f"Target:{args.target}")
print(f"Ports:{args.port} ")

result = sock.connect_ex(((args.target) , int(args.port)))
if result == 0:
 print("Host is up")
else:
 print("The host may be closed or filtered.")






