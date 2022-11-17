import os
import time

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = load_dotenv("tobi.env")




class CoverScraper:

    def __init__(self, url:str):
        service = Service('/Users/tobijohn/miniforge3/envs/soundscrape-env/bin/chromedriver')
        self.url = url
        opt = Options()
        #opt.add_argument("headless")
        self.driver = webdriver.Chrome(options=opt, service=service)
        self.driver.get(self.url)
        self.driver.maximize_window()

        
    def get_data(self):
        data = self.driver.execute_script("return window.__PRELOADED_STATE__")
        return data

    def click_element(self, xpath:str):
        '''
        Finds and clicks an element on the webpage parameters

        Parameters
        ---------
        xpath: str
            xpath of the element to be clicked
        '''
        
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def sign_in(self,username: WebElement,password: WebElement):
        '''
        Defines login credentials for signing in
        
        Parameters
        ---------
        username: webelement 
            username id
        password: webelement
            password id
        '''
      
        username.send_keys(os.environ["username"])
        password.send_keys(os.environ["password"])
        time.sleep(1)
        password.send_keys(Keys.ENTER)
        
       


    def google_search(self, topic:str):
        driver = self.driver
        input = driver.find_element(By.XPATH, '//input[@class="gLFyf gsfi"]')
        input.send_keys(topic)
        time.sleep(1)
        input.send_keys(Keys.ENTER)
         
      
        return driver

    def display(df) -> pd.DataFrame:
        """ display table in a nice way """
        pd.set_option('display.width', None)
        from IPython.display import display
        display(df)
    
    def tearDown(self):
        '''
        method to close down driver after data scraping
        '''
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
   #url = 'google.com'
   major = CoverScraper(url = 'https://www.tesco.com/') #url = 'https://www.tesco.com/'
   major.get_data()
   #major.google_search()







        

