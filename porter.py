import socket
import pyfiglet
import argparse
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)

def logo():
 print(pyfiglet.figlet_format("Porter", font="small"))
 print("by: davidoberst")
 print("")

 
logo()
