# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:42:31 2018
 
@author: gauthier
"""
 
"https://bitcointalk.org/index.php?board=1.0"
 
 
import os;
os.chdir('/Users/Gauthier/Documents/GitHub/forecast')
 
 
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

import csv

#%% Importing Threads urls and post numbers
def get_url(url):
    
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "footerarea"))
        )
    finally:
        b =driver.find_elements_by_id("quickModForm")[0].find_elements_by_tag_name("tr")
        return(b)

def page_information_extraction(b, post, id, status, activity, merit, datetime):
    
    class_page = b[0].get_attribute("class")
     
    
    c = driver.find_elements_by_class_name(class_page)
    
    # Collecting information
    
    i=1
    alert=np.nan
    
    
    for k in c :    
        
        # Debuging tool
        print(i)
        
        # Collecting the post
        post.append(k.find_element_by_class_name("post").text)
        
        
        # Colleting info about the member
        # in case there is "copper membership", we have to shift
        shift=0
        info = k.find_element_by_class_name("poster_info").text.splitlines()
        if info[2]!='':
            shift=1
        id.append(info[0])
        status.append(info[1])
        activity.append(pd.to_numeric(re.findall(r'\d+',info[5+shift])[0]))
        merit.append(pd.to_numeric(re.findall(r'\d+',info[6+shift])[0]))
        
        if i%10==0:
            if (len(post)==len(id)==len(status)==len(activity)==len(merit))==False:
                alert = i
        i=i+1
        
        # Adding information about the date
        postdate = k.find_element_by_class_name("td_headerandpost").find_element_by_class_name("smalltext").text
        postdate=postdate.replace('Today',(str(ddt.today().year)+'-'+str(ddt.today().month)+'-'+str(ddt.today().day)))
        datetime.append(pd.to_datetime(postdate))
    
    if np.isnan(alert)==False:
        print('problem happened around', i)
        
    return (post, id, status, activity, merit, datetime)

def get_url(url):
    
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "footerarea"))
        )
    finally:
        b =driver.find_elements_by_id("quickModForm")[0].find_elements_by_tag_name("tr")
        return(b)

def page_information_extraction(b, post, id, status, activity, merit, datetime):
    
    class_page = b[0].get_attribute("class")
     
    
    c = driver.find_elements_by_class_name(class_page)
    
    # Collecting information
    
    i=1
    alert=np.nan
    
    
    for k in c :    
        
        # Debuging tool
        #print(i)
        
        # Collecting the post
        post.append(k.find_element_by_class_name("post").text)
        
        
        # Colleting info about the member
        # in case there is "copper membership", we have to shift
        shift=0
        info = k.find_element_by_class_name("poster_info").text.splitlines()
        #print(info)
        if info[2]!='':
            shift=1
            if info[3]!='':
                shift=2
                if info[4]!='':
                    shift=3
        id.append(info[0])
        status.append(info[1])
        activity.append(pd.to_numeric(re.findall(r'\d+',info[5+shift])[0]))
        merit.append(pd.to_numeric(re.findall(r'\d+',info[6+shift])[0]))
        
        if i%10==0:
            if (len(post)==len(id)==len(status)==len(activity)==len(merit))==False:
                alert = i
        i=i+1
        
        # Adding information about the date
        postdate = k.find_element_by_class_name("td_headerandpost").find_element_by_class_name("smalltext").text
        postdate=postdate.replace('Today',(str(ddt.today().year)+'-'+str(ddt.today().month)+'-'+str(ddt.today().day)))
        datetime.append(pd.to_datetime(postdate))
    
    if np.isnan(alert)==False:
        print('problem happened around', i)
        
    return (post, id, status, activity, merit, datetime)

#%% Importing Threads urls and post numbers
with open('export.csv', 'r') as f1:
    reader = csv.reader(f1)
    thread = list(reader)
f1.close()

#%% Importing Threads urls and post numbers
options = webdriver.ChromeOptions()
options.add_argument('headless')
 
 
driver = webdriver.Chrome('/Users/Gauthier/Documents/CoursENSAE/3A/MOOC/Applied_marchine_learning_in_python/chromedriver') 
#driver = webdriver.Chrome(executable_path='C:\\Users\\Gauthier\\Anaconda3\\chromedriver.exe')#, chrome_options=options)

#%% Importing Threads urls and post numbers
post = []
id = []
status = []
activity = []
merit = []
datetime = []
count=0


for i in range(30):
    print(i)
    if (int(thread[i][1])<= 475):
        url = thread[i][0].rstrip()+";all"
        b = get_url(url)
        [post, id, status, activity, merit, datetime] = page_information_extraction(b, post, id, status, activity, merit, datetime)
    else:
        #Boucle à vérifier
        nb_page = int(int(thread[i][1])/20)+1
        for j in range (nb_page):
            print(j)
            url = thread[i][0].rstrip()+str(j*20)
            b = get_url(url)
            [post, id, status, activity, merit, datetime] = page_information_extraction(b, post, id, status, activity, merit, datetime)



#% Puting everything together
df = pd.DataFrame(
        {'datetime':datetime,
         'id':id,
         'status':status,
         'activity':activity,
         'merit':merit,
         'post':post})
        

driver.quit()

#%% Importing Threads urls and post numbers
df.to_csv('final_data.csv', sep=';')