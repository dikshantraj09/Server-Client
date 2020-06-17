#Run this file on the system you want to send the command from.
import os
import socket
import time
import sys

s=socket.socket()
host='192.168.0.107' #Enter the ip address of the machine you are tying to shutdown
port=96 #Same port as in the server
s.connect((host,port))
print("")
print("Connected To Server")
command=input("Enter the Command:")
s.send(command.encode())
print("Command Sent")

