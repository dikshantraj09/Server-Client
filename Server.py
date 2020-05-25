import os
import socket
import time
import sys

s=socket.socket()
print(socket.gethostname())
host=socket.gethostname()
port=8080
s.bind((host,port))
print("\n Waiting For connection ...\n\n")
s.listen(5)
conn,addr=s.accept()
print("")
print(addr,"-Connected")
print("")
''''command=input(str("Command:"))
conn.send(command.encode())
print("Command Sent. Waiting For Conformation")
print("")
data=conn.recv(1024)
if data:
    print("Shutdown Command Received")'''
    
 
command=conn.recv(1024)
command=command.decode()
print (command)
if command == "shutdown" or command=='hibernate': 
    print("")
    print("Hibernate Command")
    #os.system("shutdown /h")
else:
    print("False")
