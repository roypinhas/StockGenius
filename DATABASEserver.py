import socket

import select
import tqdm
import os
from datetime import datetime
from PredictPrice import PredictPrice
def print_client_sockets(client_sockets):
 for c in client_sockets:
    print("\t", c.getpeername())

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1728))

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
filename = 'forbes2000/csv/'+'AAPL'.upper() + '.csv'
filesize = os.path.getsize(filename)
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
            data = current_socket.recv(1024).decode()
            #data = current_socket.recv(int(data_len)-2).decode()

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
            #add protocol loop
            if True:
                # send the filename and filesize
                current_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
                symbol = data
                # start sending the file
                progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True,
                                     unit_divisor=1024)
                with open(filename, "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            # file transmitting is done
                            break
                        # we use sendall to assure transimission in
                        # busy networks

                        current_socket.sendall(bytes_read)

                        # update the progress bar
                        print(len(bytes_read))
                        time = 0
                        time = len(bytes_read) + time
                        progress.update(time)
                # close the socket
                #current_socket.send(p.predict_price(data.split()[0], data.split()[1]).encode())
            #is this needed?
            else:
                current_socket.send("Unidentified".encode())

if data == 'EXIT':
    current_socket.send("EXIT".encode())
    current_socket.close()
    server_socket.close()