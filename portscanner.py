import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter The Ip: " )
port = int(input("Please enter the port: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
