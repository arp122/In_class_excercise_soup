
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
soup = BeautifulSoup(response.text,'html')


# In[2]:

table=soup.find('table')
td=table.find_all('td')
table_data=[]
i=0
for row in td:
    table_data.append(row.string)


# In[3]:

neighbourhood=[]
j=4
while j < len(table_data):
    neighbourhood.append(table_data[j])
    j=j+5
neighbourhood=neighbourhood[:59]


# In[5]:

import sqlite3
conn = sqlite3.connect('startupsystems.db')
c = conn.cursor()

c.execute('''CREATE TABLE neighbours
             (name text)''')



# In[6]:

for element in neighbourhood:
    c.execute("INSERT INTO neighbours VALUES ('"+str(element)+"')")
conn.commit()


# In[ ]:



