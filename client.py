import os
import socket
import time
import sys

s=socket.socket()
host='192.168.0.107'
port=8080
s.connect((host,port))
print("")
print("Connected To Server")
command='shutdown'
s.send(command.encode())
