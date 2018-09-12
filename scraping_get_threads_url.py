# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:42:31 2018

The following script extracts the threads urls from a given forum
 
@author: gauthier
""" 

"https://bitcointalk.org/index.php?board=1.0"
 
 
import os;
a=os.getcwd(); # Prints the working directory
print('Current working directory:',a)
 
##Change working directory
os.chdir('/Users/Gauthier/Documents/GitHub/forecast') # Provide the path here
#a=os.getcwd(); # Prints the working directory
#print('Current working directory:',a)
 
 
#%% Importing Libraries
import numpy as np
import selenium
import time
import csv
import math
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from datetime import date as ddt
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') #replace with .Firefox(), or with the browser of your choice

#import itertools
from itertools import *
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
 
 
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') 
#driver = webdriver.Chrome(executable_path='C:\\Users\\Gauthier\\Anaconda3\\chromedriver.exe')#, chrome_options=options)

thread=[]
post_number=[]

url = 'bitcointalk.org/index.php?board=1.'

# We want to collect 500 pages (after that, last message before may 2017)

# The structure of the first page is special, we therefore treat it separately
driver.get("http://"+url.rstrip())
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "footerarea"))
    )
finally:
    b =driver.find_elements(By.XPATH, '//*[@id="bodyarea"]/div[3]/table')[0]
    for l in range (40):
        xpath =  '//*[@id="bodyarea"]/div[3]/table/tbody/tr['+str(l+2)+']/td[3]'
        xpath1 =  '//*[@id="bodyarea"]/div[3]/table/tbody/tr['+str(l+2)+']/td[5]'
        c = b.find_elements(By.XPATH, xpath)[0].find_elements_by_xpath('.//a')
        d = int(b.find_elements(By.XPATH, xpath1)[0].text)
        thread.append(c[0].get_attribute('href'))
        post_number.append(str(d+1))


# We loop to collect from page 2 to 5O0
# how to use : to go until page 500, type range (1,500)
for k in range (1,500):

    driver.get("http://"+url.rstrip()+str(k*40))
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "footerarea"))
        )
    finally:
        b =driver.find_elements(By.XPATH, '//*[@id="bodyarea"]/div[2]/table')[0]
        for l in range (2):
            xpath =  '//*[@id="bodyarea"]/div[2]/table/tbody/tr['+str(l+2)+']/td[3]'
            xpath1 =  '//*[@id="bodyarea"]/div[2]/table/tbody/tr['+str(l+2)+']/td[5]'
            c = b.find_elements(By.XPATH, xpath)[0].find_elements_by_xpath('.//a')
            thread.append(c[0].get_attribute('href'))
            d = int(b.find_elements(By.XPATH, xpath1)[0].text)
            post_number.append(str(d+1))
driver.quit()

#%% Export to csv
with open('export_url.csv', 'w', newline='') as myfile1:
     wr = csv.writer(myfile1, quoting=csv.QUOTE_ALL)
     wr.writerow(thread)
     
 with open('export_post_number.csv', 'w', newline='') as myfile2:
     wr = csv.writer(myfile2, quoting=csv.QUOTE_ALL)
     wr.writerow(post_number)
