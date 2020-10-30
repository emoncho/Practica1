#!/usr/bin/env python
# coding: utf-8

# In[31]:


#ELECCIONES 2016
import requests
page = requests.get("https://www.realclearpolitics.com/epolls/2016/president/us/general_election_trump_vs_clinton-5491.html")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


# In[32]:


print(soup.p())
soup.p['class']


# In[33]:


soup.find_all('th') #header cell, contains header information


# In[34]:


headings = [th.get_text() for th in soup.find("tr").find_all("th")]
headings


# In[35]:


datasets = []
for row in soup.find_all("tr")[1:]:
    dataset = list(td.get_text() for td in row.find_all("td"))
    datasets.append(dataset)

#CREATING THE DATAFRAME
import pandas as pd
df = pd.DataFrame(datasets, columns=headings)
df = df.drop_duplicates()
df1 = df.dropna()
df1['Month'] = df1['Date'].str.extract(r'\- (.*?)\/')
df1[['Sample Size','Sample Type']] = df.Sample.str.split(" ",expand=True,)
df1[['Winner','Spread Value']] = df.Spread.str.split(" +",expand=True,)
df1


# In[40]:


df2 = df1[['Clinton (D)', 'Trump (R)', 'Month']]
df2 =df2.drop([0,1], axis=0)
df2
type(df2['Month'])
df2['Clinton (D)'] = df2['Clinton (D)'].astype('int')
df2['Trump (R)'] = df2['Trump (R)'].astype('int')
df2['Month'] = df2['Month'].astype('category')
df2


# In[45]:


df3 = df2.groupby((df2.Month!=df2.Month.shift()).cumsum()).mean().reset_index(drop=False)
df3['Months to election'] = -df3['Month']
df3['Spread'] = abs(df3['Clinton (D)'] - df3['Trump (R)'])
df3


# In[53]:


import matplotlib.pyplot as plt
import numpy as np
plt.plot(df3['Months to election'],df3['Clinton (D)'], color='red', label = 'Democratic party')
plt.plot(df3['Months to election'],df3['Trump (R)'], color='blue', label = 'Republican party' )
plt.xlabel('Months to election')
plt.ylabel('Mean value of poll results for each month')
plt.title('Poll results (Election 2016)')
plt.legend(loc=1)
plt.show()


# In[55]:


plt.plot(df3['Months to election'],df3['Spread'], color='grey',linestyle='dashed')
plt.fill_between(df3['Months to election'],df3['Spread'], 0,
                 facecolor="grey", # The fill color
                 color='grey',       # The outline color
                 alpha=0.2)          # Transparency of the fill
plt.xlabel('Months to election')
plt.ylabel('Spread value abs(Winner-Loser)')
plt.title('Spread between candidates (Election 2016)')
plt.show()


# In[42]:


#Output to CSV format
from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
date_time


# In[12]:


df1.to_csv(str(date_time + 'elecciones2016.csv'), index = False, encoding='utf-8')
df3.to_csv(str(date_time + 'AGREG_elecciones2016.csv'), index = False, encoding='utf-8')


# In[15]:



#CREATING THE DATAFRAME
import pandas as pd
df = pd.DataFrame(datasets, columns=headings)
df = df.drop_duplicates()
df1 = df.dropna()
from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
df1.to_csv(str(date_time + 'elecciones2020.csv'), index = False, encoding='utf-8')


# In[57]:


#ELECCIONES 2020
page = requests.get("https://www.realclearpolitics.com/epolls/2020/president/us/general_election_trump_vs_biden-6247.html")
soup = BeautifulSoup(page.content, 'html.parser')
headings = [th.get_text() for th in soup.find("tr").find_all("th")]
datasets = []
for row in soup.find_all("tr")[1:]:
    dataset = list(td.get_text() for td in row.find_all("td"))
    datasets.append(dataset)
    
#CREATING THE DATAFRAME
df = pd.DataFrame(datasets, columns=headings)
df = df.drop_duplicates()
df1 = df.dropna()
df1['Month'] = df1['Date'].str.extract(r'\- (.*?)\/')
df1[['Sample Size','Sample Type']] = df.Sample.str.split(" ",expand=True,)
df1[['Winner','Spread Value']] = df.Spread.str.split(" +",expand=True,)

df2 = df1[['Biden (D)', 'Trump (R)', 'Month']]
df2 =df2.drop([0,1], axis=0)
type(df2['Month'])
df2['Biden (D)'] = df2['Biden (D)'].astype('int')
df2['Trump (R)'] = df2['Trump (R)'].astype('int')
df2['Month'] = df2['Month'].astype('category')

df3 = df2.groupby((df2.Month!=df2.Month.shift()).cumsum()).mean().reset_index(drop=False)
df3['Months to election'] = -df3['Month']
df3['Spread'] = abs(df3['Biden (D)'] - df3['Trump (R)'])

#GRAFICOS
plt.plot(df3['Months to election'],df3['Biden (D)'], color='red', label = 'Democratic party')
plt.plot(df3['Months to election'],df3['Trump (R)'], color='blue', label = 'Republican party' )
plt.xlabel('Months to election')
plt.ylabel('Mean value of poll results for each month')
plt.title('Poll results (Election 2020)')
plt.legend(loc=1)
plt.show()

plt.plot(df3['Months to election'],df3['Spread'], color='grey',linestyle='dashed')
plt.fill_between(df3['Months to election'],df3['Spread'], 0,
                 facecolor="grey", # The fill color
                 color='grey',       # The outline color
                 alpha=0.2)          # Transparency of the fill
plt.xlabel('Months to election')
plt.ylabel('Spread value abs(Winner-Loser)')
plt.title('Spread between candidates (Election 2020)')
plt.show()

#FICHEROS CSV
from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
df1.to_csv(str(date_time + 'elecciones2020.csv'), index = False, encoding='utf-8')
df3.to_csv(str(date_time + 'AGREG_elecciones2020.csv'), index = False, encoding='utf-8')


# In[ ]:




