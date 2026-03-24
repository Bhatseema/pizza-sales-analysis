#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[4]:


df = pd.read_csv("pizza_sales.csv")
print(df)


# In[35]:


df.head()


# In[36]:


df.tail()


# In[37]:


df.info()


# In[38]:


df.describe()


# In[39]:


df.isnull().sum()


# In[40]:


df.duplicated().sum()


# In[8]:


total_revenue = df["total_price"].sum()
print("Total Revenue:", total_revenue)


# In[6]:


total_orders = df["order_id"].nunique()
print("Total Orders:", total_orders)


# In[5]:


total_pizzas_sold = df["quantity"].sum()
print("Total Pizzas Sold:", total_pizzas_sold)


# In[9]:


total_orders = df["order_id"].nunique()
avg_order_value = total_revenue / total_orders
print("Average Order Value:", avg_order_value)


# In[45]:


avg_pizzas_per_order = total_pizzas_sold / total_orders
print("Average Pizzas Per Order:", avg_pizzas_per_order)


# In[46]:


df['order_date']=pd.to_datetime(df['order_date'],format='%d-%m-%Y')
df['day_week'] = df['order_date'].dt.day_name()
df['day_week']


# In[52]:


order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
orders_by_day = df.groupby('day_week')['order_id'].nunique().reindex(order)
plt.figure(figsize=(8,5))
orders_by_day.plot(kind='bar')
plt.title("Total Orders by Day of Week")
plt.xlabel("Day of Week")
plt.ylabel("Total Orders")
plt.show()


# In[53]:


df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

df["month"] = df["order_date"].dt.strftime("%B")

monthly_orders = df.groupby("month")["order_id"].nunique().reindex([
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]).reset_index()


# In[54]:


plt.figure(figsize=(12,5))
plt.plot(monthly_orders["month"], monthly_orders["order_id"], marker="o")

plt.title("Monthly Trend for Total Orders")
plt.xlabel("Month")
plt.ylabel("Total Orders")

plt.show()


# In[55]:


category_sales = df.groupby("pizza_category")["total_price"].sum()
category_sales.plot.pie(autopct='%1.1f%%')
plt.title("Percentage of Sales by Pizza Category")
plt.show()


# In[56]:


size_sales = df.groupby('pizza_size')['total_price'].sum()
size_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Percentage of Sales by Pizza Size")
plt.ylabel("")
plt.show()


# In[58]:


pizza_category_qty = df.groupby("pizza_category")["quantity"].sum().sort_values(ascending=False)
pizza_category_qty.plot(kind="bar")
plt.title("Total Pizza Sold by Category")
plt.xlabel("Category")
plt.ylabel("Total Quantity")
plt.show()


# In[63]:


import plotly.express as px
category_quantity = df.groupby('pizza_category')['quantity'].sum().reset_index()
print(category_quantity)
fig = px.funnel(
    category_quantity.sort_values(by='quantity', ascending=False),
    x='quantity',
    y='pizza_category',
    color='pizza_category',
    title='Total Pizzas Sold by Pizza Category'
)
fig.show()


# In[65]:


top_revenue = df.groupby("pizza_name")["total_price"].sum().sort_values(ascending=False).head(5)
top_revenue.plot(kind="bar")
plt.xlabel("Pizza Name")
plt.ylabel("Revenue")
plt.title("Top 5 Best Selling Pizzas by Revenue")
plt.show()


# In[66]:


top_quantity = df.groupby("pizza_name")["quantity"].sum().sort_values(ascending=False).head(5)
top_revenue.plot(kind="bar")
plt.xlabel("Pizza Name")
plt.ylabel("quantity")
plt.title("Top 5 Best Selling Pizzas by quantity")
plt.show()


# In[67]:


top_quantity = df.groupby("pizza_name")["order_id"].sum().sort_values(ascending=False).head(5)
top_revenue.plot(kind="bar")
plt.xlabel("Pizza Name")
plt.ylabel("orders")
plt.title("Top 5 Best Selling Pizzas by Orders")
plt.show()


# In[68]:


bottom5 = df.groupby('pizza_name')['total_price'].sum().sort_values().head(5)
bottom5.plot(kind='bar')
plt.title("Bottom 5 Worst Selling Pizzas by Revenue")
plt.xlabel("Pizza Name")
plt.ylabel("Revenue")
plt.show()


# In[69]:


bottom5 = df.groupby('pizza_name')['order_id'].sum().sort_values().head(5)
bottom5.plot(kind='bar')
plt.xlabel("Pizza Name")
plt.ylabel("orders")
plt.title("Bottom 5 Worst Selling Pizzas by orders")
plt.show()


# In[10]:


top_quantity = df.groupby("pizza_name")["quantity"].sum().sort_values(ascending=False).head(5)
top_quantity.plot(kind="bar")
plt.title("Top 5 worst Selling Pizzas by Quantity")
plt.xlabel("Pizza Name")
plt.ylabel("Quantity Sold")
plt.show()


# In[ ]:




