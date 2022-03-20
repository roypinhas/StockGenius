import socket
import tqdm
import socket

import os
from Search import SearchMechanism
#connect everything - todo
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
s = SearchMechanism()
symbol = s.search()


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
my_socket.connect(('127.0.0.1', 1728))
print(1)
#loop until exit  input - send to server and print answer
while True:
    clientChoose = str(symbol)

    print(clientChoose)
    my_socket.send(clientChoose.encode())
    #data = my_socket.recv(1024)
    # receive the file infos
    # receive using client socket, not server socket
    received = my_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    # remove absolute path if there is
    filename = os.path.basename(filename)
    # convert to integer
    filesize = int(filesize)

    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = my_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    print(received)
    if clientChoose == "EXIT":
        break

my_socket.close()