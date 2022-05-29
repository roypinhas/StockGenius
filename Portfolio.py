class Portfolio:

    path = '/Users/roypinhas/Desktop/pythonProject/credentials/'
    def __init__(self, username):
        self.username = username

    #this needs to be sent to a files server wherre you store the username/password
    def add_symbol(self, symbol):
        if self.symbol_exists(symbol):
            return False
        file1 = open(self.path + str(self.username) + ".txt", 'r')
        lines = file1.readlines()
        print(lines)
        file1 = open(self.path + str(self.username) + ".txt", 'w+')

        for i in range(len(lines)):
            #print(lines[i])
            file1.write(str(lines[i]))

        file1.write(str(symbol).upper())
        file1.write('\n')
        ''''for x in symbols:
            file1.write(x.upper())
            file1.write('\n')'''''
        return True
    def symbol_exists(self,symbol):
        p = self.get_portfolio()
        for x in p:
            if x==symbol.upper():
                return True
        return False

    def get_portfolio(self):
        file1 = open(self.path + str(self.username) + ".txt", 'r')
        lines = file1.readlines()

        portfolio = []

        for i in range(7,len(lines)):
            print('i:' + str(i))
            portfolio.append(lines[i][:len(lines[i]) - 1])#[:len(lines[i]) - 2]

        return portfolio

#p = Portfolio('erer')
#ss = ['aapl','tsla','intu','amzn']
#print(p.get_portfolio())
