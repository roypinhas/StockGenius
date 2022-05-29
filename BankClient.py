import socket
class BankClient:

    #create a client - some of values are optional - not needed for all actions
    def __init__(self, reg_type, creditcard_number=None, expiration_date=None, security_code=None,sum=None):

        self.creditcard_number = creditcard_number
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.sum = sum
        self.reg_type = reg_type

    def run(self):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect to server
        my_socket.connect(('127.0.0.1', 1879))

        print('type:'  + str(self.reg_type))
        if self.reg_type == 'CREATE':
            contents = 'Type:' + str(self.reg_type) + ',' + "CreditcardNumber:"+str(self.creditcard_number)+',' +'ExpirationDate:'+str(self.expiration_date)+','  +'SecurityCode:'+str(self.security_code)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
            print('sent')
        elif self.reg_type == 'CHANGE':
            contents = 'Type:' + str(self.reg_type) + ',' + "CreditcardNumber:" + str(self.creditcard_number) + ',' + 'ExpirationDate:' + str(
                self.expiration_date) +','  +'SecurityCode:'+str(self.security_code) +','  +'Sum:'+str(self.sum)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())

        data_len = my_socket.recv(11).decode()

        data_len = data_len[7:10]

        if int(data_len[0]) == 0:
            data_len = data_len[1:]
        if int(data_len[0]) == 0:
            data_len = data_len[1:]

        data = my_socket.recv(int(data_len)).decode()

        while len(data) != int(data_len):
            data = data + my_socket.recv(int(data_len) - len(data))

        datas = data.split(',')
        answer = datas[0][8:]

        print("closed")
        my_socket.close()
        return answer
