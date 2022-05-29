import socket
import random
import select
import re
from datetime import datetime
from PredictPrice import PredictPrice
from register import Register
from datetime import datetime
from Payment import Payment
from Portfolio import Portfolio
class UserServer:



    def print_client_sockets(self, client_sockets):
            for c in client_sockets:
                print("\t", c.getpeername())

    def run(self):
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(("0.0.0.0", 1849))

            server_socket.listen(1)
            print("listening for clients..")
            client_sockets = []
            messages_to_send = []

            p = PredictPrice()

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

                        data = current_socket.recv(1024).decode().replace(' ','')
                        print('d: ' + str(data))
                        datas = data.split(',')
                        if len(data) >0:
                            datas = datas[1:]
                            print(datas)
                            request = datas[0].split(':')[1]
                        # loop until you get the wanted length (check the length of the data each time)
                        '''''''''''
                        print("hereUserServer")
                        data_len = current_socket.recv(11).decode()
                        if len(data_len) >  0:
                            data_len = data_len[7:10]
                            print("datalen:" + str(data_len))
                            if int(data_len[0]) == 0:
                               data_len = data_len[1:]
                            if int(data_len[0]) == 0:
                                data_len = data_len[1:]
                            
                            #todo - how do i do the loop thing (cant other things get i?)
                            data = current_socket.recv(int(data_len)).decode()
                            #i dont think this is how youdoit
                            while len(data) != int(data_len):
                                data = data + current_socket.recv(int(data_len)-len(data))
                            datas = data.split(',')
                            request = datas[0][5:]
                        '''''''''''
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
                        print(datas[1])

                        if request == 'SIGNUP':
                            username = datas[1].split(':')[1]
                            password = datas[2].split(':')[1]
                            email = datas[3].split(':')[1]
                            r = Register(username, password, email)
                            answer = str(r.signup())
                            contents = "Message:"+answer

                            message = str('Length:'+str(len(contents)).zfill(3) +',' + contents)
                            current_socket.send(message.encode())

                        elif request == 'LOGIN':
                            username = datas[1].split(':')[1]
                            password = datas[2].split(':')[1]
                            r = Register(username, password, None)

                            answer = str(r.login())
                            contents = "Message:" + answer
                            message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                            current_socket.send(message.encode())
                            #current_socket.send(answer.encode())
                        elif request == 'CANCEL':
                            username = datas[1].split(':')[1]

                            r = Payment(username)

                            answer = str(r.remove_subscription())
                            contents = "Message:" + answer
                            message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                            current_socket.send(message.encode())
                            #current_socket.send(answer.encode())

                        elif request == 'PAYMENT':
                            username = datas[1].split(':')[1]
                            creditcard_num = datas[2].split(':')[1]
                            expiration_date = datas[3].split(':')[1]
                            security_code = datas[4].split(':')[1]
                            p = Payment(username,creditcard_num,expiration_date,security_code)
                            if p.check_creditcard_num() and p.check_securitycode() and p.check_expirationdate():
                                p.save_info()
                                answer = True
                            else:
                                answer = False

                                contents = "Message:" + str(answer)
                                message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                                current_socket.send(message.encode())
                                #current_socket.send(str(True).encode())



                        elif request == 'ADDSYMBOL':
                            username = datas[1].split(':')[1]
                            symbol = datas[2].split(':')[1]
                            p =  Portfolio(username)
                            worked = p.add_symbol(symbol)
                            #check if file exists!!??
                            contents = "Message:" + str(worked)
                            message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                            current_socket.send(message.encode())
                            #current_socket.send(str(True).encode())
                        elif request == 'GETPORTFOLIO':
                            username = datas[1].split(':')[1]
                            p = Portfolio(username)
                            answer = str(p.get_portfolio())
                            contents = "Message:" + answer
                            message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                            print('message: '+message)
                            current_socket.send(message.encode())

                        elif request == 'GETPAYMENT':
                            username = datas[1].split(':')[1]
                            answer = Payment(username).get_payment()
                            contents = "Message:" + str(answer)
                            message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                            print('message: ' + message)
                            current_socket.send(message.encode())

                            #current_socket.send(p.get_portfolio().encode())







            if data == 'EXIT':
                current_socket.send("EXIT".encode())
                current_socket.close()
                server_socket.close()

s = UserServer()
s.run()