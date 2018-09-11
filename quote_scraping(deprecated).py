#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:20:47 2018

@author: Gauthier
"""

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
import pandas as pd
from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor


#%% Setting up and launching the scraper
# Setup Chrome
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') #replace with .Firefox(), or with the browser of your choice

# Go to the website
driver.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20180911')

# It is important to wait to let the page load. However, better to use more precise functions such as Web Driver Wait
time.sleep(2)

# We extract the HTML
innerHTML = driver.execute_script("return document.body.innerHTML")

# We quit the selenium browser
driver.quit()


#%% Setting up and launching the parser
# We parse the data using BeautifulSoup
soup = BeautifulSoup(innerHTML, 'lxml')
table_doc = soup

# We extract the table
extractor = Extractor(table_doc)
extractor.parse()
table=extractor.return_list()