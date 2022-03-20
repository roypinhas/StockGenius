import socket
from Search import SearchMechanism

s = SearchMechanism()
symbol = s.search()
date = s.getDate()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server
my_socket.connect(('127.0.0.1', 1729))
print(1)
#loop until exit  input - send to server and print answer
while True:
    clientChoose = str(symbol) + " " + str(date)
    clientChoose = str(len(clientChoose)) + str(clientChoose)
    print(clientChoose)
    my_socket.send(clientChoose.encode())
    data = my_socket.recv(1024)

    print(data.decode())
    if clientChoose == "EXIT":
        break

my_socket.close()