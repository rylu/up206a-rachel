#!/usr/bin/env python
# coding: utf-8

# 

# 

# In[1]:


# for general data wrangling tasks
import pandas as pd

# to read and visualize spatial data
import geopandas as gpd

# to provide basemaps 
import contextily as ctx

# to give more power to your figures (plots)
import matplotlib.pyplot as plt


# Import jobs dataset

# In[2]:


ffjobs = gpd.read_file('CBP2018.CB1800CBP_2021-01-23T142924_Extended_Filtered.csv')


# In[3]:


ffjobs.info()


# Import county boundaries dataset

# In[4]:


counties = gpd.read_file('CA_Counties_TIGER2016.shp')


# In[5]:


counties.info()


# In[6]:


counties.plot()


# In[7]:


counties.tail(100)


# In[8]:


ffjobs['NAME'].value_counts()


# In[9]:


ffjobs[ffjobs.NAME == 'Los Angeles County, California']


# Because the jobs dataset does not contain values for the geometry field, we will splice geometry data from the county dataset into the corresponding county row in the ffjobs dataset. 
# 
# We can see that the values in the GEOID column from the counties dataset correspond to the last five digits of the GEO_ID column from the ffjobs dataset. So, we must first isolate the last 5 digits of the GEO_ID field for each row in ffjobs. Then, we will find the corresponding GEOID in the county dataset. Finally, we will set the geometry field in the ffjobs dataset equal to the corresponding geometry data in the county dataset. 

# In[10]:



# create a for loop to iterate through each row and run the following code. 
for index, row in ffjobs.iterrows():
    
    # create a new variable 'geomid' to store the value of GEO_ID for a row 
    geomid = row["GEO_ID"]
    
    # isolate the last 5 digits of the GEO_ID column from the ffjobs dataset. 
    last_digits = geomid[-5:]
    
    # check to make sure we have the right digits. 
    print(last_digits)
    
    # create a new variable 'countyrow' that finds the collection of rows in county dataset where 
    # GEOID is equal to the last 5 digits in the ffjobs dataset. In other words, we are creating a 
    # dataframe containing the single row in the counties dataset that corresponds to last_digits 
    countyrow = counties[counties.GEOID == last_digits]

    # df1.loc[[0], 'geometry'] = df2.loc[[0], 'geometry']
    ffjobs.loc[[index], "geometry"] = countyrow["geometry"].values

ffjobs


# 

# In[23]:


# use subplots that make it easier to create multiple layered maps
fig, ax = plt.subplots(figsize=(15, 15))

# turn the axis off
ax.axis('off')

# set a title
ax.set_title('Fossil Fuel Employment by County Map ',fontsize=16)

# add a basemap
counties.plot(alpha=0.5, color = 'white', edgecolor ='grey', ax=ax)

# oilandgas = ffjobs[ffjobs.NAICS2017_LABEL == 'Oil and gas extraction']
ffjobs.plot(column = 'EMP',
            alpha=0.75, 
            legend = True, 
            linewidth = 1, 
            cmap = 'twilight', 
            edgecolor='grey',
            figsize=(12,10),
            ax=ax)


# In[16]:


# use subplots that make it easier to create multiple layered maps
fig, ax = plt.subplots(figsize=(15, 15))

# turn the axis off
ax.axis('off')

# set a title
ax.set_title('Fossil Fuel Employment by County Map ',fontsize=16)

# add a basemap
counties.plot(alpha=0.5, color = 'white', edgecolor ='grey', ax=ax)
petroleum = ffjobs[ffjobs.NAICS2017_LABEL == 'Petroleum refineries']
petroleum.plot(column = 'EMP',
            alpha=0.75, 
            legend = True, 
            linewidth = 1, 
            cmap = 'twilight', 
            edgecolor='grey',
            figsize=(12,10), ax=ax)


# In[ ]:





# In[ ]:





# In[ ]:




