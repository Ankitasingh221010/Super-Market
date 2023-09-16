#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loading the datasheet
import pandas as pd #importing panda library
df=pd.read_csv("C:/Users/user/Downloads/supermarket sales Sheet1.csv")
df


# In[2]:


df1=df.copy()
df1


# In[3]:


df.size


# In[4]:


df.shape


# In[5]:


df.head(10)


# In[6]:


df.describe()


# In[7]:


# is your supermarket more popular with males or females?
#counting the gender count
g=df['Gender'].value_counts() #counting the total no. of men and women
g


# In[8]:


import seaborn as sns
sns.countplot(x=df['Gender'])
#plt.title("Total Number Of Male And Female")


# In[9]:


# what does the customer rating look like and can you also comment on its skewness?
import seaborn as sns #importing seaborn 
import numpy as np # importing numpy library
sns.distplot(df['Rating'])


# In[10]:


#conclusion- There is slight skewness around right side and majority of rating is densed around 6.5


# In[11]:


get_ipython().run_line_magic('pinfo', 'branches')


df["Branch"].value_counts() #branch value count


# In[12]:


import matplotlib.pyplot as plt
sns.countplot(x=df['Branch']) #plotting the count plot
plt.title("Count Vs Branch") #title of the plot


# In[13]:


# which is the most popular payment method used by customers?

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.countplot(x=df['Payment'])
plt.title("Count Vs Method of Payment")
plt.xlabel("Method of Payment")
plt.ylabel("count")


# In[14]:


a=df["Payment"].value_counts() #payment made by different mean count
a


# In[15]:


# find branch wise payment method distribution inall branches

plt.figure(figsize = (14,6))
plt.style.use('classic')
ax = sns.countplot(x = "Payment", hue = "Branch", data= df, palette= "tab20")
ax.set_title(label = "Payment distribution in all Branches", fontsize=25)
ax.set_xlabel(xlabel = "payment method", fontsize=16)
ax.set_ylabel(ylabel = "People Count", fontsize= 16)
              


# In[16]:


#customer type in branches
plt.figure(figsize = (14,6))
plt.style.use('classic')
ax = sns.countplot(x = "Customer type", hue = "Branch", data= df, palette= "rocket_r")
ax.st_title(label = "Customer type in diffrent Branches", fontsize=25)
ax.set_xlabel(xlabel = "Branches", fontsize=16)
ax.set_ylabel(ylabel = "customer Count", fontsize= 16)
              


# In[23]:


# does gross income affect customer ratings?

r=df["Rating"]
r


# In[27]:


#find rating distribution between branches
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8,4))
ax = sns.boxplot(x="Branch", y="Rating",data=df,palette='RdYlBu')
ax.set_title("Rating distribution between Branches", fontsize=25)
ax.set_xlabel(xlabel = "Branches",fontsize=16)
ax.set_ylabel(ylabel = "Rating distribution", fontsize=16)
plt.grid()


# # Q1 find the distribution between branches.

# In[29]:


sns.set_style('darkgrid')
sns.scatterplot(x=df['Rating'], y=df['gross income'])
plt.show()


# # Q2 what is the most profitable branch?

# In[30]:


sns.boxplot(x=df['Branch'], y=df['gross income'])
plt.title("Gross income Vs Branch")


# # Q3 how is the relationship between Gender and Gross income?

# In[31]:


sns.boxplot(x=df['Gender'], y=df['gross income'])
plt.title("Gross income Vs Gender")


# # Q4 can you see any time trend in gross income?

# In[32]:


df.groupby(df.index).mean()


# In[33]:


sns.lineplot(x=df.groupby(df.index).mean().index,
            y = df.groupby(df.index).mean()['gross income'])


# # conclusion- gross income value fluctuate lot

# # Q5 which product line help you generate the most income?

# In[36]:


cat=df[["Product line","gross income"]].groupby(['Product line'], as_index=False).sum().sort_values(by='gross income',ascending=False)
plt.figure(figsize=(20,8))
sns.barplot(x='Product line', y='gross income',data=cat)
plt.title("Gross income Vs Product line")


# # Q6 what is the spending pattern of both males and females,meaning in which category do they spend more?

# In[37]:


plt.figure(figsize=(16,6))
plt.title('total monthly transaction by Gender')
sns.countplot(x=df['Product line'], hue=df.Gender)


# # conclusion-female spending more fashion accessories and male more spending on health and beauty 

# # Q7 how many products are bought by customers?

# In[56]:


xdata = [1,2,3,4,5,6,7,89,10]
plt.figure(figsize = (12,6))
sns.distplot(x=df['Quantity'])


# # which day of the week has maximum sales?

# In[39]:


df['Date']=pd.to_datetime(df['Date'])


# In[40]:


df['weekday']=df['Date'].dt.day_name()


# In[41]:


df.set_index('Date', inplace=True)


# In[42]:


df.head()


# In[43]:


plt.figure(figsize=(8,6))
plt.title('Daily sales by day of the week')
sns.countplot(x=df['weekday'])


# # conclusion- sale is highest on saturday

# # Q9 which hour of the day is busiest? 

# In[44]:


df['Time'] = pd.to_datetime(df['Time'])
df['Hour'] = (df['Time']).dt.hour
df['Hour'].unique()


# In[45]:


sns.lineplot(x="Hour", y='Quantity',data=df).set_title("Product sales per Hour")


# # peak is observed in the 14th hour 2pm 

# # Q10 which prouduct line should your supermarket focus on?

# In[46]:


xdata = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize =(12,6))
sns.barplot(y= df['Product line'], x=df['Rating'])


# # conclusion- Food and beverages and fashion accessories 

# # Q11 which city should be chosen for expansion and what products should be focusses?

# In[52]:


plt.figure(figsize=(20,7))
ax = sns.barplot(x=df1['City'],y=df1['gross income'], palette='Set1')
plt.xlabel("City name", fontsize='16')
plt.xticks(fontsize='16')
plt.ylabel('Gross income', fontsize='16')
plt.yticks(fontsize='16')


# In[55]:


plt.figure(dpi=125)
sns.countplot(y = 'Product line', hue = 'City', data=df)
plt.xlabel('Count')
plt.show()


# In[ ]:




