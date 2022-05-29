from csv import reader
import pickle
from StockEvaluation import StockEvaluation
class Recommendations:

    def __init__(self, csv_name):
        self.effs = []
        self.csv_name = csv_name
    def get_accuracy(self, symbol):
        loaded_model = pickle.load(open('/Users/roypinhas/Desktop/pythonProject/' + symbol.upper() + 'model.pkl', 'rb'))
        return loaded_model.coef_

    def run(self):
        counter = 0
        # open file in read mode
        with open(self.csv_name, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                #need to remove - temporary #todo bevause not all the files have models yet (needs to be length of file not 10)
                if counter < 10:
                    counter = counter +1
                    symbol = row[0]
                    # row variable is a list that represents a row in csv
                    a = float(self.get_accuracy(str(symbol)))
                    self.effs.append(StockEvaluation(symbol,a))
                    print(a)

    # Function returns N largest elements
    def Nmaxelements(self,list1, N):
        final_list = []

        for i in range(0, N):
            max1 = StockEvaluation('',0)

            for j in range(len(list1)):
                if list1[j].get_accuracy() > max1.get_accuracy():
                    max1 = list1[j];

            list1.remove(max1);
            final_list.append(max1.to_string())

        print(final_list)
        return tuple(final_list)

#r = Recommendations('symbols2.csv')
#r.run()
#print("best:")
#r.Nmaxelements(r.effs, 5)