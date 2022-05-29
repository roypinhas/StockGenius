import pandas as pd #handle data
import yfinance as yf
from datetime import datetime, timedelta
from csv import writer
import pickle
import csv
from csv import reader
from moveFolder import ManageFile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from os.path import exists


class PricePrediction:

    #gets file with names of symbols to calculate
    def __init__(self,csv_name):
        self.csv_name = csv_name

    #loops the prediction method 7 times to calculate for the next week
    def week_prediction(self, symbol):
        for i in range(7):
            self.predict(symbol,i)

    #predicts for the given symbol the future given date (i=days)
    def predict(self, symbol, days):
        file1 = open("specifications.txt", 'r')
        lines = file1.readlines()
        path = lines[3]+'/pythonProject/stock_market_data/forbes2000/csv/'+symbol.upper() + '.csv'
        try:
            df = pd.read_csv(path)
            len_before = len(df.index)#

            #
            if days == 0:
                dt = datetime.now()
                td = timedelta(days=-1)
                my_date = dt + td
                dt = datetime.now().strftime("%Y-%m-%d")
                data = yf.download(symbol, str(dt))
                price = data['Adj Close'][0]
                #
            else:
                r = csv.reader(open(path))  # Here your csv file
                lines = list(r)
                row_count = sum(1 for row in r)
                price = lines[row_count - 1][6]


            dt = datetime.now()

            td = timedelta(days=days)
            #calculated date
            my_date = dt + td

            row_contents = [my_date.strftime("%d/%m/%Y"), 0, 0, 0, 0, 0, price]
            self.append_list_as_row(path, row_contents)

            df = pd.read_csv(path)
            len_after = len(df.index)


            df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)
            df = df[['Adjusted Close']]

            #ema
            df.ta.ema(close='Adjusted Close', length=10, append=True)

            #drop the rows with NaN as a result of ema
            df = df.iloc[10:]

            #splitting the data to training and testing (80/20)
            X_train, X_test, y_train, y_test = train_test_split(df[['Adjusted Close']], df[['EMA_10']],
                                                                test_size=0.2, shuffle=False)

            #train model
            model = LinearRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            r = csv.reader(open(path))
            lines = list(r)
            row_count = sum(1 for row in r)
            lines[row_count-1][6] = float(y_pred[len(y_pred)-1])
            writer = csv.writer(open(path, 'w'))
            writer.writerows(lines)
            #validating
            #Print metrics
            print("Model Coefficients:", model.coef_)
            print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
            print("Coefficient of Determination:", r2_score(y_test, y_pred))
            pickle.dump(model, open(lines[3]+'/pythonProject/'+symbol.upper() + 'model.pkl', 'wb'))

        except:

            lines = list()

            members = symbol

            with open(self.csv_name, 'r') as readFile:

                reader = csv.reader(readFile)

                for row in reader:

                    lines.append(row)

                    for field in row:

                        if field == members:
                            lines.remove(row)

            with open(self.csv_name, 'w') as writeFile:

                writer = csv.writer(writeFile)

                writer.writerows(lines)


    #run over the file with all the stock symbols
    def run(self):
        file1 = open("specifications.txt", 'r')
        lines = file1.readlines()
        # open file in read mode
        with open(self.csv_name, 'r') as read_obj:

            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:

                # row variable is a list that represents a row in csv
                if exists(lines[3]+'/pythonProject/' + str(row[0]) +"model.pkl"):
                    m = ManageFile()
                    m.deletePreviousFile(lines[3]+'/pythonProject/' +str(row[0])+"model.pkl")

                #self.predict(str(row[0]))
                self.week_prediction(str(row[0]))

    def append_list_as_row(self, file_name, list_of_elem):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)


#pp = PricePrediction("/Users/roypinhas/Desktop/pythonProject/symbols2.csv")
#pp.run()