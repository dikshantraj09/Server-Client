#Run this file on the system you want to send the command from.
import os
import socket
import time
import sys

s=socket.socket()
host='serveo.net'
port=9632
s.connect((host,port))
print("")
print("Connected To Server")
command=input("Enter the Command:")
s.send(command.encode())
print("Command Sent")

