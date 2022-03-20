import socket
import random
import select
from datetime import datetime
from PredictPrice import PredictPrice
def print_client_sockets(client_sockets):
 for c in client_sockets:
    print("\t", c.getpeername())

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1729))

server_socket.listen(1)
print("listening for clients..")
client_sockets = []
messages_to_send = []

p = PredictPrice()

#gets inout from clients and sends them  back answer according to their input (using select)
data = ' '
while data != "EXIT":
    rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])

    for current_socket in rlist:
        if current_socket is server_socket:
            connection, client_address = current_socket.accept()
            print("New client joined!", client_address)
            client_sockets.append(connection)
            print_client_sockets(client_sockets)
        else:
            #loop until you get the wnated length (check the length of the data each time)
            data_len = current_socket.recv(2).decode()
            data = current_socket.recv(int(data_len)).decode()
            while int(len(str(data))) != int(data_len):#len(str(data)) != data_len:


                data = str(data) + str(current_socket.recv(int(data_len) -len(str(data))).decode())


            if data == "":
                print("Connection closed",)
                client_sockets.remove(current_socket)
                current_socket.close()
                print_client_sockets(client_sockets)
            else:
                messages_to_send.append((current_socket, data))

    for message in messages_to_send:
        current_socket, data = message
        if current_socket in wlist:
            print(data)

            messages_to_send.remove(message)
            if True:
                print(98)
                current_socket.send(p.predict_price(data.split()[0], data.split()[1]).encode())
                print(9)
            #is this needed?
            else:
                current_socket.send("Unidentified".encode())

if data == 'EXIT':
    current_socket.send("EXIT".encode())
    current_socket.close()
    server_socket.close()