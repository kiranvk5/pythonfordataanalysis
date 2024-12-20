# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:29:15 2024

@author: Lenovo
"""
"""
----How many sales they have made with amounts more than 1000?
----How many sales they have made that belong to the category "Tops" and have a quantity of 3
----The total sales by category
----Average amount by category and status
----Total Sales by fulfilment and shipment type



  
"""
import pandas as pd

#Load the sales data from the excel file into a pandas DataFrame

sales_data = pd.read_excel('/Users/Lenovo/Desktop/Python course/Amazon Sales Project/sales_data.xlsx')

sales_data.info()

sales_data.describe()

#looking at columns
print(sales_data.columns)

#having a look at the first few rows of  data
print(sales_data.head())

#check the data types of the columns
print(sales_data.dtypes)


# =================================================================
# cleaning the data
# ===============================================================
 

# check for missing values in our sales data

sales_data.isnull().sum()

# if amount has null it need to be  removed and promotion id has
# alot of null value and its not important, so whole of column can be emoved 
# but as aamount is important column in amazon sales, only null has to be removed

#drop any rows that has any missing/nan values
sales_data_dropped = sales_data.dropna() 

#drop rows with missing amounts based on the amount columns
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

#check for missing values in our sales data cleaned
print(sales_data_cleaned.isnull().sum())

# ===============================================================
# Aggregating the Data
# ===============================================================

#total sales by category
category_totals = sales_data.groupby('Category')['Amount'].sum()
category_totals = sales_data.groupby('Category', as_index=False)['Amount'].sum() 
category_totals = category_totals.sort_values('Amount', ascending = False)

#calculate the average Amount by category and Fulfilment
fulfilment_average = sales_data.groupby(['Category','Fulfilment'], as_index=False)['Amount'].mean()
fulfilment_average = fulfilment_average.sort_values('Amount',ascending=False)

#calculate the average Amount by Category and Status
status_averages = sales_data.groupby(['Category','Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount',ascending=False)


#total sales by shipment and fulfilment
total_sales_shipandfulfilment = sales_data.groupby(['Courier Status','Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandfulfilment = total_sales_shipandfulfilment.sort_values('Amount',ascending=False)
total_sales_shipandfulfilment.rename(columns={'Courier Status' : 'Shipment'},inplace=True)

# ======================================================
#Exporting the Data
# ======================================================

status_averages.to_excel('average_sales_by_category_and_status.xlsx',index=False)
total_sales_shipandfulfilment.to_excel('total sales by shipment and fulfilment.xlsx',index =False)