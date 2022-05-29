from datetime import datetime
import re
class Payment:
    PATH = '/Users/roypinhas/Desktop/pythonProject/credentials/'
    def __init__(self,username, creditcard_num=None, expiration_date=None, security_code=None):
        self.username = username
        self.creditcard_num = str(creditcard_num).replace('-','')
        self.expiration_date = expiration_date
        self.security_code = security_code

    def save_info(self):
            print("IN SAVE INFO")
            file1 = open(self.PATH + str(self.username) + ".txt", 'r')
            lines = file1.readlines()
            print(lines)
            file1 = open(self.PATH + str(self.username) + ".txt", 'w+')

            '''for i in range(len(lines)):
                print(lines[i])
                file1.write(str(lines[i]))'''
            for i  in range (3):
                file1.write((str(lines[i])))

            if len(lines) <=3:
                file1.write('\n')
            file1.write(str(self.creditcard_num))
            file1.write('\n')
            file1.write(str(self.expiration_date))
            file1.write('\n')
            file1.write(str(self.security_code))
            file1.write('\n')
            file1.write(str(datetime.now()))
            file1.write('\n')


            for i in range (7, len(lines)):
                file1.write(str(lines[i]))

    def check_expirationdate(self):

        month = self.expiration_date.split('/')[0]
        year = self.expiration_date.split('/')[1]
        current_month = datetime.now().month
        current_year = int(datetime.now().year) -2000
        if len(month) ==2 and len(year) == 2 and month.isnumeric() and year.isnumeric() and int(month) < 13 and int(month) >0 and int(year) > 0:
            if current_year < int(year):
                return True
            if current_year == int(year) and int(current_month) < int(month):
                return True
        return False

    def check_securitycode(self):
        if len(self.security_code) == 3 and self.security_code.isnumeric():
            return True
        return False

    #neends to be in format: 1234-5678-....
    def check_creditcard_num(self):


            pattern = '^[456][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'

            result = re.match(pattern, self.creditcard_num)
            if result:
                return True
            else:
                return False

    def remove_subscription(self):

        file1 = open(self.PATH + str(self.username) + ".txt", 'r')
        lines = file1.readlines()
        print(lines)
        file1 = open(self.PATH + str(self.username) + ".txt", 'w+')

        '''for i in range(len(lines)):
            print(lines[i])
            file1.write(str(lines[i]))'''
        for i in range(len(lines)):
            if i != 6:
                file1.write((str(lines[i])))
            else:
                file1.write(str('FALSE'))

        return True


    def get_payment(self):
        file1 = open(self.PATH + str(self.username) + ".txt", 'r')
        lines = file1.readlines()
        p = lines[3:7]
        return p