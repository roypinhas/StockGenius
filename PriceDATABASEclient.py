import socket
class PriceClient:

    def __init__(self,  reg_type, symbols=None, symbol=None,days=None):
        self.symbols = symbols
        self.symbol = symbol
        self.days = days
        self.reg_type = reg_type

        '''if self.symbols != None:
            self.reg_type = 'GETSUGGESTIONS'
        elif self.symbol != None:
            self.reg_type = 'GETPRICE'''''




    def run(self):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect to server
        my_socket.connect(('127.0.0.1', 1841))

        print('type:'  + str(self.reg_type))
        if self.reg_type == 'GETSUGGESTIONS':
            contents = 'Type:' + str(self.reg_type) + ',' + "Symbols:"+str(self.symbols)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
            print('sent')
        elif self.reg_type == 'GETPRICE':
            contents = 'Type:' + str(self.reg_type) + ',' + "Symbol:" + str(self.symbol) + ',' + 'Days:' + str(
                self.days)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())



        data_len = my_socket.recv(11).decode()
        print("data_lemn:" + str(data_len))
        data_len = data_len[7:10]
        print("data_lemn:" + str(data_len))
        if int(data_len[0]) == 0:
            data_len = data_len[1:]
        if int(data_len[0]) == 0:
            data_len = data_len[1:]
        print("hereUserClient")
        data = my_socket.recv(int(data_len)).decode()
        # i dont think this is how youdoit
        while len(data) != int(data_len):
            data = data + my_socket.recv(int(data_len) - len(data))

        if self.reg_type != 'GETSUGGESTIONS':
            datas = data.split(',')
            answer = datas[0][8:]
        else:
            answer = data[10:len(data)-1].replace("'", "").replace(",","").split(' ')
            print(answer)
        print("closed")
        my_socket.close()
        return answer

