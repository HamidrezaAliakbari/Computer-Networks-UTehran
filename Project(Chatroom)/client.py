import socket 
import sys 
import pickle
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
IP_address = str(input('Please enter your desired IP address:'))
Port = int(input('Please enter your desired PORT NO. :')) 
server.connect((IP_address, Port))
name = input("enter your name:\n")
server.sendall(name.encode('utf-8'))
  
while True: 
  
    mode = int(input("1.List  2.Send\n3.Recieve   4.Exit\n"))

    if  mode == 1:
        server.sendall(b"List")
        List = server.recv(1024)
        print("List of clients:\n")
        print(pickle.loads(List))
    elif mode == 2:
        server.sendall(b"Send")
        recvName = input("Enter contact name:\n")
        message = input("Type your message:\n")
        server.sendall(recvName.encode('utf-8'))
        if server.recv(2048) == b"1":
        	server.sendall(message.encode('utf-8'))
        else:
        	print("Error occured\n")
    elif mode == 3:
        server.sendall(b'recieve')
        recv_message = server.recv(1024)
        print(pickle.loads(recv_message))
    elif mode == 4:
        break
    else:
        print("entery is not registered")

server.close() 