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
#import itertools
from itertools import *
import time
 
#%% 
options = webdriver.ChromeOptions()
#options.add_argument('headless')
 
 
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') #replace with .Firefox(), or with the browser of your choice
url = 'bitcointalk.org/index.php?topic=2851721.0;all'
url= 'bitcointalk.org/index.php?topic=454795.0;all'
 
driver.get("http://"+url.rstrip())

 
#%% 
a=driver.find_elements_by_id("quickModForm")
 
b =driver.find_elements_by_id("quickModForm")[0].find_elements_by_tag_name("tr")
 
#%% Identifying each post
l=[]
 
len(b)
for i in b:
    l.append(i.get_attribute("class") )
    
class_page = l[0]
 

c = driver.find_elements_by_class_name(class_page)

#%% Collecting post text
c[0].find_element_by_class_name("post").text
post = []
 
for k in c :
    post.append(k.find_element_by_class_name("post").text)
    
#%% Collecting information about the member
id = []
status = []
activity = []
merit = []
i=1

for k in c :
    # in case there is "copper membership", we have to shift
    shift=0
    print(i)
    info = k.find_element_by_class_name("poster_info").text.splitlines()
    if info[2]!='':
        shift=1
        print('shift')
    print(info)
    id.append(info[0])
    status.append(info[1])
    activity.append(pd.to_numeric(re.findall(r'\d+',info[5+shift])[0]))
    merit.append(pd.to_numeric(re.findall(r'\d+',info[6+shift])[0]))
    i=i+1
    
#%% Collecting information about the date
datetime = []

for k in c :
    datetime.append(pd.to_datetime(k.find_element_by_class_name("td_headerandpost").find_element_by_class_name("smalltext").text))

#%% Puting everything together
df = pd.DataFrame(
        {#'datetime':datetime,
         'id':id,
         'status':status,
         'activity':activity,
         'merit':merit,
         'post':post})
    
#%% We exit the driver
info[3]==''
