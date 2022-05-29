import os
import smtplib
from validate_email_address import validate_email
from TwoFactorAuthentication import TwoFA
class Register:

    path = '/Users/roypinhas/Desktop/pythonProject/credentials/'

    def __init__(self, username_input, password_input, email_input):
        self.username_input = username_input
        self.password_input = password_input
        self.email_input = email_input



    #check subscription

    def signup(self):

        if not str(self.username_input).isalnum():
            return False

        if os.path.exists(self.path + self.username_input+'.txt'):

            return str('exists')


        isvalid = validate_email(self.email_input)
        isExists = validate_email(self.email_input, verify=True)


        if not isvalid and not isExists:
            return False

        f = open(self.path + str(self.username_input) + ".txt", "w+")
        f.write(str(self.username_input))
        f.write('\n')
        f.write(str(self.password_input))

        f.write('\n')
        f.write(str(self.email_input))

        return True

    def check_password(self):
        # Using readlines()
        file1 = open(self.path + str(self.username_input) + ".txt", 'r')
        lines = file1.readlines()
        if self.password_input == lines[1]:
            return True
        return False

    def check_username(self):
        if not str(self.username_input).isalnum():
            return False
        if not os.path.exists(self.path + self.username_input+'.txt'):
            return False
        return True

    def get_email(self):

        file1 = open(self.path + str(self.username) + ".txt", 'r')
        lines = file1.readlines()

        return lines[2]


    def login(self):

        if not self.check_username() or not self.check_password():
            return False
        fa = TwoFA()

        return fa.fa(self.get_email(),"royp444@gmail.com", 12345)


