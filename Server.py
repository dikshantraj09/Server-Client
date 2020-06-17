import os
import socket
import time
import sys


s=socket.socket()
print(socket.gethostname())
host='0.0.0.0'
port=96
s.bind((host,port))
print("\n Waiting For connection ...\n\n")
s.listen(9)
conn,addr=s.accept()
print("")
print(addr,"-Connected")
print("")
 
command=conn.recv(1024)
command=command.decode()
print (command)
if command == "shutdown" or command=='hibernate': 
    print("")
    print("Shutdown Command Recieved")
    os.system("shutdown /s")
wlif command=='hibernate': 
    print("")
    print("Hibernate Command Recieved")
    os.system("shutdown /h")  
else:
    print("No or wrong Command")
