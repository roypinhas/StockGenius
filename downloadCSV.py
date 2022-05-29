from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os.path
from os import path

#download new updated file
class downloadCSV:

    def download(self):
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : "<directory_path>"};
        #example: prefs = {"download.default_directory" : "C:\Tutorial\down"};
        options.add_experimental_option("prefs",prefs);
        driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=options);

        try:

            driver.get('https://www.kaggle.com/paultimothymooney/stock-market-data');

            #gotit= driver.find_element_by_id('accept-cookie-notification');
            print(4)

            #gotit.click();

            #downlaod try1
            driver.implicitly_wait(3)
            downloadcsv = driver.find_element(by=By.XPATH, value='//*[@id="site-container"]/div/div[1]/div[2]/div[2]/div/div[1]/a/button');#'//*[@id="site-content"]/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a/button');
            downloadcsv.click();

            #login  - select email option
            downloadcsv2 = driver.find_element_by_xpath('//*[@id="site-container"]/div[1]/div/form/div[2]/div/div[2]/a/li/div');
            downloadcsv2.click();

            driver.implicitly_wait(3)

            #enter email
            downloadcsv25 = driver.find_element_by_xpath('//*[@id="site-container"]/div[1]/div/form/div[2]/div[1]/div/label/input');
            downloadcsv25.click()
            #downloadcsv25.clear()
            downloadcsv25.send_keys('royp444@gmail.com')
            downloadcsv25.send_keys(Keys.ENTER)

            #enter password
            downloadcsv3 = driver.find_element_by_xpath('//*[@id="site-container"]/div[1]/div/form/div[2]/div[2]/div/label/input');
            downloadcsv3.click();
            downloadcsv3.send_keys("04042004")
            downloadcsv3.send_keys(Keys.ENTER)

            #download try2
            downloadcsv = driver.find_element_by_xpath('//*[@id="site-content"]/div[3]/div[5]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]');#'//*[@id="site-content"]/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a/button');
            downloadcsv.click();

            found = False
            while not found:

                found = path.exists("/Users/roypinhas/Downloads/archive.zip")
            


            #driver.close()'''

        except Exception as e:
            print(e)
            print("Invalid URL")


#t = downloadCSV()
#t.download()