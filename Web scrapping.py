#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the required libraries

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

#getting the webpage:

url='https://fred.stlouisfed.org/categories'

#download the url

response=requests.get(url)

response.status_code

len(response.text)

page_content=response.text

with open('webpage.html','w') as f:
    f.write(page_content)                 # storing the page in a file in html format
    
doc=BeautifulSoup(page_content,'html.parser')    #using beautiful soup

type(doc)

data_title_tags=doc.find_all('p',class_='fred-categories-children')

data_title_lists=[]
links_list = []
for tags in data_title_tags:
    data_links_tags = doc.find_all("span", class_="fred-categories-child")


for links in data_links_tags:
    children = links.findChildren("a" , recursive=False)
    for child in children:
        links_list.append('https://fred.stlouisfed.org/'+child['href'])
        data_title_lists.append(child.text)
# print(data_title_lists[:7])
# print(links_list[:7])

import pandas as pd

csv_dict = {
    'title': data_title_lists[:7],
    'links': links_list[:7]
}
df = pd.DataFrame(csv_dict)
df
df.to_csv('csv_dict.csv')

