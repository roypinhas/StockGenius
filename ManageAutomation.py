from downloadCSV import downloadCSV
from moveFolder import ManageFile
from PriceAlgorithm import PricePredictionAuto
class Automation:

    #manage automation of csv update
    def __init__(self):
        d = downloadCSV()
        d.download()
        m = ManageFile()



a = Automation()

