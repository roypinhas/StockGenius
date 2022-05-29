import socket
import select
from Bank import Bank

class BankServer:

    def print_client_sockets(self, client_sockets):
        for c in client_sockets:
            print("\t", c.getpeername())

    def run(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 1879))

        server_socket.listen(1)
        print("listening for clients..")
        client_sockets = []
        messages_to_send = []

        # gets inout from clients and sends them  back answer according to their input (using select)
        data = ' '
        while data != "EXIT":
            rlist, wlist, xlist = select.select([server_socket] + client_sockets, client_sockets, [])

            for current_socket in rlist:
                if current_socket is server_socket:
                    connection, client_address = current_socket.accept()
                    print("New client joined!", client_address)
                    client_sockets.append(connection)
                    self.print_client_sockets(client_sockets)
                else:

                    data = current_socket.recv(1024).decode().replace(' ', '')
                    datas = data.split(',')
                    if len(data) > 0:
                        datas = datas[1:]

                        request = datas[0].split(':')[1]

                    if data == "":
                        print("Connection closed", )
                        client_sockets.remove(current_socket)
                        current_socket.close()
                        self.print_client_sockets(client_sockets)
                    else:
                        messages_to_send.append((current_socket, data))

            for message in messages_to_send:
                current_socket, data = message
                if current_socket in wlist:
                    print(data)

                    messages_to_send.remove(message)

                    print("request: "+str(request))

                    #change balance of money of given user's bank account
                    if request == 'CHANGE':
                        creditcard_num = datas[1].split(':')[1]
                        expiration_date = datas[2].split(':')[1]
                        security_code = datas[3].split(':')[1]
                        sum = datas[4].split(':')[1]
                        b = Bank(creditcard_num, expiration_date, security_code)
                        answer = str(b.change_balance(sum))
                        contents = "Message:" + answer

                        message = str('Length:' + str(len(contents)).zfill(3) + ',' + contents)
                        print('messageee:'+message)
                        current_socket.send(message.encode())



                    #Create a new account in the bank
                    elif request == 'CREATE':
                        creditcard_num = datas[1].split(':')[1]
                        expiration_date = datas[2].split(':')[1]
                        security_code = datas[3].split(':')[1]

                        b = Bank(creditcard_num, expiration_date, security_code)

                        answer = str(b.create())
                        contents = "Message:" + answer
                        message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                        current_socket.send(message.encode())


        if data == 'EXIT':
            current_socket.send("EXIT".encode())
            current_socket.close()
            server_socket.close()


s = BankServer()
s.run()