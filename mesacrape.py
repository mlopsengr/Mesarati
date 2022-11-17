import json
import os
import shutil
import time
import urllib.request
from email.mime import image
from lib2to3.pgen2 import driver
from pickle import NONE
from tkinter.ttk import Style
from unicodedata import name
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2


import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from dataclasses import dataclass

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from this import d

from utils.scrape import CoverScraper


class Mesascrape(CoverScraper):
    def __init__(self):
       CoverScraper.__init__(self, url = 'https://en.wikipedia.org/wiki/List_of_Maserati_vehicles')


    def get_num_rows(self):
        '''
        gets number or rows on a table
        '''
        time.sleep(1)
        driver = self.driver
        delay = 10
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mw-content-text']/div[1]/table[1]"))) 
            num_rows = len(driver.find_elements(By.XPATH, ".//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr"))
            print("Rows in table are " + repr(num_rows))
        except TimeoutException:
            print("Table took too long to load") 

        return num_rows
            


    def get_data(self):
        time.sleep(1)
        driver = self.driver

        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, 2 * document.body.scrollHeight);")
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 3 * document.body.scrollHeight);")

        num_rows = self.get_num_rows()

        mesatable = pd.DataFrame(columns=['displacement','power'])

        before_XPath = "//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr["
        aftertd_XPath = "]/td["
        aftertr_XPath = "]"

        for t_row in (1, num_rows):
            displacement_FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(6) + aftertr_XPath
            power__FinalXPath = before_XPath + str(t_row) + aftertd_XPath + str(7) + aftertr_XPath
            displace_ment = driver.find_element(By.XPATH, displacement_FinalXPath).text
            pow_er = driver.find_element(By.XPATH, power__FinalXPath).text
            mesatable['displacement'].update(displace_ment)
            mesatable['power'].update(pow_er)
            
        return mesatable



class Mesanalytics():
    def __init__(self):

        pass

    def data_extract(self):
        mesadata = pd.read_excel(r'Mesarati Data.xlsx',sheet_name= 'Sheet2')
        mesadata = pd.DataFrame(mesadata)

        return mesadata

    def data_upload(self):
        mesadata = self.data_extract()
        # upload data to postgressql 
        conn = psycopg2.connect(database='tobijohn', user='postgres', password='postgres', host='localhost', port='5432')
        mesadata.to_sql('tobijohn', con=conn, if_exists='replace', index=False)

        return mesadata








    

if __name__ == '__main__':
    
    mesa = Mesanalytics()
    mesa.data_upload()
