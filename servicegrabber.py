
import socket

s = socket.socket()

ip =input("Please enter the ip: ")
port= str(input("Please enter the port: "))

if s.connect_ex((ip, int(port))):
   print ("No Service is running in that port")
else :
    print ("Service is "+str(s.recv(1024)).strip('b'))
    

