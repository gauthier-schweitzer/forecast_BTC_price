# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:42:31 2018
 
@author: gauthier
"""
 
"https://bitcointalk.org/index.php?board=1.0"
 
 
import os;
a=os.getcwd(); # Prints the working directory
print('Current working directory:',a)
 
##Change working directory
#os.chdir('c:\\Users\uname\desktop\python') # Provide the path here
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
#options.add_argument('headless')
 
 
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') 
#driver = webdriver.Chrome(executable_path='C:\\Users\\Gauthier\\Anaconda3\\chromedriver.exe')#, chrome_options=options)



def get_url(url):
    
    driver.get("http://"+url.rstrip())
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "footerarea"))
        )
    finally:
        print('success')
        b =driver.find_elements(By.XPATH, '//*[@id="bodyarea"]/div[3]/table')
        return(b[0])

def page_information_extraction(b):
    
    class_page = b[0].get_attribute("class")
     
    
    c = driver.find_elements_by_class_name(class_page)
    
    
        
# We exit the driver
url = 'bitcointalk.org/index.php?board=1.0'

#page_information_extraction(url)
#driver.quit()
b=1
b = get_url(url)
b.find_elements_by_class_name("windowbg3")[0].text
#c = b.find_elements_by_tag_name('a')[0].find_elements_by_tag_name('href')[0].text


#c=b.find_elements_by_tag_name('a')[0].text


#b.find_elements_by_class_name("windowbg3")[0].text
#page_information_extraction(b)
driver.quit()

# //*[@id="bodyarea"]/div[3]/table

#//*[@id="bodyarea"]/div[2]/table
