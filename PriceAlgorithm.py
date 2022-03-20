import pandas as pd #handle data
import pandas_ta
import sklearn
import numpy
import pandas_to_sql
import pickle
from csv import reader
from moveFolder import ManageFile
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from statsmodels.tsa.ar_model import AutoReg
from Search import SearchMechanism
from os.path import exists
#works but need to remove problematic files.
class PricePredictionAuto:

    '''def __init__(self):
        #getting data
        s = SearchMechanism()
        symbol = s.search()
        date = self.getDate()
        price = self.predict(symbol,date)'''


    def __init__(self,csv_name):
        self.csv_name = csv_name
        self.run(csv_name)

    def predict(self,symbol):
        df = pd.read_csv('forbes2000/csv/'+symbol.upper() + '.csv')
        #parse_dates=[0],infer_datetime_format=True
        #preparing data
        print(type(df['Date'][0]))

        df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)
        df = df[['Adjusted Close']]

        #add technical indicators - ema
        df.ta.ema(close='Adjusted Close', length=10, append=True)

        #drop the rows with NaN
        df = df.iloc[10:]

        #splitting data to training and testing (80/20)
        X_train, X_test, y_train, y_test = train_test_split(df[['Adjusted Close']], df[['EMA_10']],
                                                            test_size=.2, shuffle=False)
        #begin training
        model = LinearRegression()
        model.fit(X_train, y_train)
        #print("x: " + X_test)
        print("x")
        print(X_test)
        y_pred = model.predict(X_test)

        print("results " + str(y_test))
        print(y_pred)
        #validating
        # Printout relevant metrics
        print("Model Coefficients:", model.coef_)
        print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
        print("Coefficient of Determination:", r2_score(y_test, y_pred))

        #trying to save
        pickle.dump(model, open(symbol.upper() + 'model.pkl', 'wb'))


    def run(self,csv_name):

        # open file in read mode
        with open(csv_name, 'r') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                if exists(str(row[0]) +"model.pkl"):
                    m = ManageFile()
                    m.deletePreviousFile(str(row[0])+"model.pkl")

                self.predict(str(row[0]))
#deletes files for some reason?????
pp = PricePredictionAuto("symbols2.csv")
#pp.__init__("symbols2.csv")
#pp.run()