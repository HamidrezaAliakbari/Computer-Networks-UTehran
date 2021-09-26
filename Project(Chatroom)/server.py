import socket 
import sys 
from _thread import *
import pickle

MAX_REACHED = 128
MSG_SIZE = 2048
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

IP_address = str(input('Please enter your desired IP address:'))
Port = int(input('Please enter your desired PORT NO. :')) 
server.bind((IP_address, Port))
print(f'Server binded to IP address of {IP_address} and PORT NO. of {Port} Successfully!')

server.listen(MAX_REACHED) 
name_msg = {}
client_name = {}
def send_list(list):
    ALL = pickle.dumps(list)
    return ALL

def find_connection(recv_name):
    return client_name.keys()[client_name.values().index(recv_name)]

def print_msg_name(name):
    for msg in range(len(name_msg.keys())/2):
        new_msg = new_msg + '<' + name_msg[name][2*msg] +'>' + ' ' + name_msg[name_msg][2*msg+1] + '\n'
    new_msg[name].clear()
    return new_msg
def listenToClient(connection, name,address): 
    while True: 
        mode = connection.recv(MSG_SIZE)
        if mode == b"List":
            try:
                connection.sendall(send_list(client_name.values()))
            except:
                connection.close() 
                remove(connection, name) 
        elif mode == b"Send":
            recv_name = connection.recv(MSG_SIZE).decode('utf-8')
            connection.sendall(b"1")
            recv_message = connection.recv(MSG_SIZE).decode('utf-8')
            recv_conn = find_conn(recv_name)
            send_message = recv_message + "\n"
            if name in name_msg.keys():
                name_msg[name].append(recv_name)
                name_msg[name].append(recv_message)
            else:
                name_msg[name]=[recv_name]
                name_msg[name].append(recv_message)

            try:
                recv_conn.sendall(pickle.dumps(send_message))
            except: 
                recv_conn.close() 
                remove(recv_conn, recv_name)
        elif mode == b"recieve":
            send_msg = print_msg_name(name)
            try:
                connection.sendall(pickle.dumps(send_message))
            except:
                connection.close()
                remove(connection,name)
           
def remove(connection, name): 
    del client_name[connection]
    del name_msg[name]
  
while True: 
    connection, address = server.accept() 
    name = connection.recv(MSG_SIZE).decode('utf-8')
    client_name[connection]=name
    print(address[0] + " connected")
    start_new_thread(listenToClient,(connection,name,address))     
  
connection.close() 
server.close() 