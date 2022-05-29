from moveFolder import ManageFile
import os
from downloadCSV import downloadCSV
from MonthlyPayment import MonthlyPayment
from PriceAlgorithm import PricePrediction

#this runs everyday at 12:00 using cmd action
class Automation:

    #manage automation of csv update

    def run(self):
        file1 = open("specifications.txt", 'r')
        lines = file1.readlines()

        # updating csv file
        d = downloadCSV()
        d.download()

        #remove previous file
        m = ManageFile()
        file = "stock_market_data"
        location = lines[3]+"/pythonProject"
        path = os.path.join(location, file)
        m.deletePreviousFile(path)

        #place new file
        src_path = lines[4]+"/stock_market_data.zip"
        dst_path = lines[3]+"/pythonProject/stock_market_data.zip"
        m.move(src_path, dst_path)
        st = lines[3]+ "/pythonProject/stock_market_data.zip"
        m.extract(st)
        #algo
        PricePrediction(lines[3]+'/pythonProject/symbols2.csv').run()
        mp = MonthlyPayment()
        mp.run()



a = Automation()

