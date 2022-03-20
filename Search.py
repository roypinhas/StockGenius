import csv
import datetime
class SearchMechanism:

    def getDate(self):
        pause = False
        while not pause:
            pause = True
            time = input("Do you want to know the price in a DAY/WEEK/MONTH/YEAR")
            if time.lower() == 'day':
                time = int(1)
            elif time.lower() == 'week':
                time = int(7)
            elif time.lower() == 'month':
                time = int(30)
            elif time.lower() == 'year':
                time = int(365)
            else:
                pause = False
                print("Invalid Input")

        return datetime.date.today() + datetime.timedelta(days=time)


    #check if a string contains only letters
    def checkString(self,s):
        for x in range (len(s)):

            if s[x].isalpha() is False:
                return False
        return True

    #enter characters, display top 5 matches, enter digit of result
    def search(self):

        pause = True

        reader = csv.reader(open('symbols2.csv', 'r'))
        prevResults = []
        while pause:
            print(str(1)+str(pause))
            inp = input("Enter characters/number of symbol:")
            print(inp.isdigit())

            if inp.isdigit():
                if int(inp) >0 and int(inp) <= 5:
                    symbol = str(prevResults[int(inp)-1])[2:]
                    print(str(symbol))
                    return symbol
                    pause = False
                    print("change:"+str(pause))
                else:
                    print("Invalid Entrance")

            elif self.checkString(inp):
                inp = inp.upper()
                found = False
                counter = 0
                startcount = False
                arr = []

                for row in reader:

                    if found is True:
                        break
                    p = row[0]

                    if p.startswith(inp) and counter == 0:
                        counter = 0
                        startcount = True
                    if startcount is True:
                        counter=counter+1

                        arr+= [str(counter) + '.' + str(p)]
                    if counter == 5:
                        found = True

                for x in range(len(arr)):
                    print(arr[x])

                prevResults = arr

            else:
                print("Invalid Entrance")












