import shutil
import zipfile
import os
from os.path import exists
class ManageFile:


    #manage entire process
    '''def __init__(self, src_path, dst_path ):

        self.prevFile = prevFile
        self.src_path = src_path
        self.dst_path = dst_path

        self.deletePreviousFile(prevFile)
        self.move(src_path,dst_path)
        self.extract()'''

    #move zip file from downloads to project folder
    def move(self,src_path,dst_path):
        #move zip
        #src_path = r"/Users/roypinhas/Downloads/archive.zip"
        #dst_path = r"/Users/roypinhas/Desktop/pythonProject/archive.zip"
        shutil.move(src_path, dst_path)

    #extract zip file
    def extract(self, src_path):
        #st = "/Users/roypinhas/Desktop/pythonProject/archive.zip"
        a = src_path.split('/')
        s = '/'
        b = s.join(a[:len(a) - 1])
        with zipfile.ZipFile(src_path, 'r') as zip_ref:
            #zip_ref.extractall(r"/Users/roypinhas/Desktop/pythonProject/")
            zip_ref.extractall(b)

    #delete previous CSV file
    def deletePreviousFile(self,path):
        if exists(path):
            # file = "stock_market_data"
            #LOCATION = "/Users/roypinhas/Desktop/pythonProject"
            # path = os.path.join(location, file)
            os.remove(path)
            #shutil.rmtree(path)

