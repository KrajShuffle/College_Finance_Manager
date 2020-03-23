#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as py


# In[2]:


def modify_columns(excel):
    """Function which cleans the current columns and renames orignal columns to column labels used in the future 
    
    Parameters
    ----------
    excel : dataframe
        A dataframe object which has different labels than the labels used in future functions
    
    Return
    ------
    kraj : dataframe
        A dataframe object whose column labels were adjusted to be usable in future functions
    """
    
    first_column = excel.columns[0] # first_column takes the name of the input file's first column
    second_column = excel.columns[1] # second_column takes the name of the input file's second column
    
    # Following line of code was modified from: https://www.geeksforgeeks.org/how-to-rename-columns-in-pandas-dataframe/ 
    excel.rename(columns = {first_column : 'Expenses from Previous Week', second_column : 'Initial Cash Amount'}, inplace = True)
    
    # Following line of code was taken from: https://stackoverflow.com/questions/52657272/pandas-add-a-column-with-only-one-row
    excel['Initial Cash Amount'] = excel['Initial Cash Amount'].fillna('') #Fills column with empty space instead of NAN
    
    kraj = excel
    
    return kraj


# In[3]:


def remodel_spreadsheet(excel):
    """Function which adds three columns: Total Expense from Last Week, Balance, and Number of Items Purchased with their values
    
    Parameters
    ----------
    excel : dataframe
        A dataframe object which lacks a right-most column delineating the number of weeks till bankrupt
        
    Return
    ------
    kraj : dataframe
        A dataframe object which is edited to have a right-most column with the number of weeks till bankrupt
    """
    
    excel['Total Expense from Last Week'] = ''
    # Following line was modified from https://www.geeksforgeeks.org/python-pandas-dataframe-sum/#:~:targetText=Pandas%20dataframe.,the%20values%20in%20each%20column.
    excel.loc[1,'Total Expense from Last Week'] = excel['Expenses from Previous Week'].sum(axis = 0) # First value of "Total Expense" colum is sum of "Expense from Previous Week"
    
    excel['Balance'] = ''
    excel.loc[1,'Balance'] = excel.loc[1,'Initial Cash Amount'] - excel.loc[1,'Total Expense from Last Week']
    
    excel['Number of Items Purchased'] = ''
    #Following code line was developed with help from source: https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
    num_items_purchased = excel.shape[0] # excel.shape[0] indicates the number of rows

    excel.loc[1, 'Number of Items Purchased'] = num_items_purchased # the first value of this column is num_items_purchased
    
    kraj = excel
    
    return kraj


# In[4]:


def weeks_till_bankrupt(excel):
    """Function determines how many weeks are left till the user is bankrupt if her or she spends at their current rate
    
    Parameters
    ----------
    excel : dataframe
        A dataframe object which lacks a right-most column delineating the number of weeks till user is bankrupt
    
    Return
    ------
    kraj : dataframe
        A dataframe object which is edited to have a right-most column with the value for number of weeks till user is bankrupt
    """
    
    excel['Weeks till Bankrupt'] = '' #Creating an Empty Column
    
    num_safeweeks = excel.loc[1, 'Initial Cash Amount'] // excel.loc[1, 'Total Expense from Last Week'] #Assuming a constant rate and obtaining only the whole number
    excel.loc[1, 'Weeks till Bankrupt'] = num_safeweeks # First value of 'Weeks till Bankrupt' is num_safeweeks
    
    kraj = excel

    return kraj


# In[ ]:




