#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


df = pd.read_csv('G:\Python Data Analysis\Python Sales Analysis\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding = 'unicode_escape')


# In[7]:


df.shape


# In[10]:


df.head(7)


# In[11]:


df.info()


# In[15]:


# drop unrelated/blank columns
df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[16]:


df.info()


# In[18]:


# Check for null Values
pd.isnull(df)


# In[19]:


# Check for null Values
pd.isnull(df).sum()


# In[20]:


# Drop null values
df.dropna(inplace=True)


# In[21]:


pd.isnull(df).sum()


# In[23]:


#change datatype
df['Amount'] = df['Amount'].astype('int')


# In[24]:


df['Amount'].dtypes


# In[25]:


df.columns


# In[26]:


#Rename Columns
df.rename(columns={'Marital_Status':'Married' })


# In[27]:


#Returns the description of the data. i.e. Mean, std, count
df.describe()


# In[30]:


#Use describe for specific functions
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# ## Gender Based

# In[31]:


sns.countplot(x='Gender',data=df)


# In[33]:


ax = sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[38]:


sales_gender = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender',y='Amount',data = sales_gender)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# ## Age

# In[44]:


sns.countplot(data = df, x = 'Age Group', hue = 'Gender')


# In[43]:


ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


#Total Amount vs Age Group
sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending = False)

sns.barplot(x='Age Group', y='Amount', data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs

# ## State

# In[51]:


# total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index = False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)

sns.set(rc={'figure.figsize': (15,5)})

sns.barplot(x = 'State', y = 'Orders', data = sales_state)


# In[54]:


# total amount of sales from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(b ='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})

sns.barplot(x = 'Amount', y = 'State', data = sales_state)


# ## Marital Status

# In[59]:


df.columns


# In[61]:


ax = sns.countplot(data = df, x='Marital_Status')

for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')


# ## Occupation

# In[64]:


ax= sns.countplot(data=df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[68]:


sales_state = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')


# ## Product Category

# In[70]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data=df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[72]:


sales_state = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(data=sales_state, x='Product_Category', y='Amount')


# In[74]:


fig1,ax1 = plt.subplots(figsize=(12,7))

df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# #### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
