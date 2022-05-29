import random
from os.path import exists

class Bank:

    PATH = '/Users/roypinhas/Desktop/pythonProject/Bank/'
    FILE_FIRST_CHARACTER = 'c'

    def __init__(self, creditcard_num, expiration_num, security_code):
        self.creditcard_num = str(creditcard_num).replace('-','')
        self.expiration_num = expiration_num
        self.security_code = security_code

    #check if the given account exists
    def valid_account(self):

        if not exists(self.PATH + 'c' + str(self.creditcard_num) + ".txt"):
            return False

        file1 = open(self.PATH + 'c' + str(self.creditcard_num) + ".txt", 'r')
        lines = file1.readlines()

        if lines[0].replace('\n','') != self.creditcard_num:
            return False

        if lines[1].replace('\n','') != self.expiration_num:
            return False

        if lines[2].replace('\n','') != self.security_code:
            return False

        return True

    #create a new account
    def create(self):

        f = open(self.PATH + str(self.FILE_FIRST_CHARACTER) + str(self.creditcard_num) + ".txt", "w+")
        f.write(str(self.creditcard_num))
        f.write('\n')
        f.write(str(self.expiration_num))

        f.write('\n')
        f.write(str(self.security_code))

        f.write('\n')

        #randomize account balance
        max_balance = 1000000
        f.write(str(random.randint(0,max_balance)))
        print("Account created.")
        return True


    #deposit or withdraw money in the user's bank account
    def change_balance(self, sum):
        try:
            valid = self.valid_account()

            file1 = open(self.PATH + str(self.FILE_FIRST_CHARACTER) + str(self.creditcard_num) + ".txt", 'r')
            lines = file1.readlines()

            file1 = open(self.PATH + str(self.FILE_FIRST_CHARACTER) + str(self.creditcard_num) + ".txt", 'w+')

            for i in range(len(lines)-1):
                file1.write(str(lines[i]))

            file1.write(str(int(lines[len(lines)-1])+int(sum)))

            if valid:
                print('Deposit went through.')
        except:
            return False

        return valid





