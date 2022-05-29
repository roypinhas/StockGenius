from UserClient import UserClient
from BankClient import BankClient
import os
import datetime
class MonthlyPayment:

        MONTHLY_PRICE = -10
        DIRECTORY = '/Users/roypinhas/Desktop/pythonProject/credentials'
        def charge_user(self, username):
                info = UserClient('GETPAYMENT',username=username).run()
                if info[3]=='FALSE':
                        return False
                dates = info[3].split('-')
                date = datetime.date(int(dates[0]), int(dates[1]), int(dates[2]))
                today = datetime.date.today()
                print(9)
                print(today)
                if today == date:
                        return False
                print(str((date - today)).split(' ')[0])
                if int(str((today - date)).split(' ')[0]) < 30:
                        return False

                BankClient('CHANGE',creditcard_number=info[0],expiration_date=info[1],security_code=info[2],sum=self.MONTHLY_PRICE).run()
                UserClient("PAYMENT",username=username,creditcard_num=info[0],expiration_date=info[1],security_code=info[2]).run()
                return True

        def run(self):
                for filename in os.scandir(self.DIRECTORY):
                        if filename.is_file():

                                name = (filename.name).replace('.txt','')
                                print(name)
                                if name[0] != '.':
                                        c =self.charge_user(name)



#m = MonthlyPayment().run()
