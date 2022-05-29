import socket
class UserClient:

    def __init__(self, reg_type, username=None, password=None, email=None,creditcard_num=None,
                 expiration_date=None,security_code=None,symbol=None):
        self.email = email
        self.username = username
        self.password = password
        self.creditcard_num = creditcard_num
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.symbol = symbol
        self.reg_type = reg_type

        '''if self.symbol != None:
            self.reg_type = 'ADDSYMBOL'
        elif self.creditcard_num != None:
            self.reg_type = 'PAYMENT'
        elif self.email != None:
            self.reg_type = 'SIGNUP'
        elif self.password !=  None:
            self.reg_type = 'LOGIN'
        elif self.username != None:
            self.reg_type = 'GETPORTFOLIO'''

    '''''''''
    def __init__(self, username, creditcard_num, expiration_date, security_code):
        self.reg_type = 'PAYMENT'
        self.creditcard_num = creditcard_num
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.username = username

    def __init__(self, username, password, email):
        self.reg_type = 'SIGNUP'
        self.email = email
        self.username = username
        self.password = password

    def __init__(self, username, password):
        self.reg_type = 'LOGIN'
        self.username = username
        self.password = password

    def __init__(self, username, symbol):
        self.reg_type = 'ADDSYMBOL'
        self.username = username
        self.symbol = symbol

    def __init__(self, username):
        self.reg_type = 'GETPORTFOLIO'
        self.username = username
    '''''

    def run(self):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect to server
        my_socket.connect(('127.0.0.1', 1849))

        print('type:'  + str(self.reg_type))
        if self.reg_type == 'SIGNUP':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:"+str(self.username)+',' +'Password:'+str(self.password)+','  +'Email:'+str(self.email)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
            print('sent')
        elif self.reg_type == 'LOGIN':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username) + ',' + 'Password:' + str(
                self.password)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
        elif self.reg_type == 'PAYMENT':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username) + ',' + 'CreditCardNumber:' + str(
                self.creditcard_num) + ',' + 'ExpirationDate:' + str(self.expiration_date) + ',' + 'SecurityCode:'+str(self.security_code)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
        elif self.reg_type == 'ADDSYMBOL':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username) + ',' + 'Symbol:' + str(
            self.symbol)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
        elif self.reg_type ==  'GETPORTFOLIO':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
        elif self.reg_type ==  'GETPAYMENT':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())
        elif self.reg_type ==  'CANCEL':
            contents = 'Type:' + str(self.reg_type) + ',' + "Username:" + str(self.username)
            my_socket.send(('Length:' + str(len(contents)).zfill(3) + ',' + str(contents)).encode())


        #loop until exit  input - send to server and print answer

        #is an id needed too?

        data_len = my_socket.recv(11).decode()
        data_len = data_len[7:10]

        if int(data_len[0]) == 0:
            data_len = data_len[1:]
        if int(data_len[0]) == 0:
            data_len = data_len[1:]
        print("hereUserClient")
        data = my_socket.recv(int(data_len)).decode()
        # i dont think this is how youdoit
        print(data)
        print(self.reg_type)
        while len(data) != int(data_len):

            data = data + my_socket.recv(int(data_len) - len(data))
        if self.reg_type != 'GETPORTFOLIO' and self.reg_type != 'GETPAYMENT':
            datas = data.split(',')
            answer = datas[0][8:]
        elif self.reg_type == 'GETPORTFOLIO':
            answer = data[10:len(data)-1].replace("'", "").replace(",","").split(' ')
            print(answer)
        elif self.reg_type == 'GETPAYMENT':
            print(3)
            n = '\n'
            answer = data[10:len(data)-1].replace("'","").replace(',','').split(' ')
            for i in range(len(answer)):
                if i!=3:
                    answer[i] = answer[i][0:len(answer[i])-2]
        print("closed")
        my_socket.close()
        return answer

#s = UserClient('GETPAYMENT', username="jijjjjj")
#print(s.run())