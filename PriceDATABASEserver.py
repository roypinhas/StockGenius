import socket
import random
import select
import re
from datetime import datetime
from PredictPrice import PredictPrice
from decimal import Decimal
from register import Register
from datetime import datetime
from Payment import Payment
from Portfolio import Portfolio
from recommendation import Recommendations

class PriceServer:

    NUM_OF_SUGGESTIONS = 10
#NEED TO CHECK THE NUMBER OF DAYS IS OKAY MAYBE NOT MINUS 1 OR MAYBE MINUS 2 OR 0
    def get_price(self, symbol, days):
        csv_reader = open('/Users/roypinhas/Desktop/pythonProject/forbes2000/csv/'+symbol.upper() + '.csv','r')
        list_csv_rows = []
        for row in csv_reader:
            list_csv_rows.append(row)

        print(list_csv_rows[len(list_csv_rows)-(7-int(days))])
        return round(Decimal(list_csv_rows[len(list_csv_rows)-(7-int(days))].split(',')[6]),2)

    def print_client_sockets(self, client_sockets):
        for c in client_sockets:
            print("\t", c.getpeername())

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 1841))

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

                    data = current_socket.recv(1024).decode().replace(' ', '')
                    print('d: ' + str(data))
                    datas = data.split(',')
                    if len(data) > 0:
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

                    if request == 'GETPRICE':
                        symbol = datas[1].split(':')[1]
                        day = datas[2].split(':')[1]

                        #r = Register(username, password, email)
                        answer = str(self.get_price(symbol,day))
                        contents = "Message:" + answer
                        message = str('Length:' + str(len(contents)).zfill(3) + ',' + contents)
                        current_socket.send(message.encode())

                    elif request == 'GETSUGGESTIONS':
                        file_path = datas[1].split(':')[1]

                        r = Recommendations(file_path)
                        r.run()
                        answer = str(r.Nmaxelements(r.effs, self.NUM_OF_SUGGESTIONS))
                        contents = "Message:" + answer
                        message = 'Length:' + str(len(contents)).zfill(3) + ',' + contents
                        current_socket.send(message.encode())
                        # current_socket.send(answer.encode())


                        # current_socket.send(p.get_portfolio().encode())

        if data == 'EXIT':
            current_socket.send("EXIT".encode())
            current_socket.close()
            server_socket.close()


s = PriceServer()

s.run()