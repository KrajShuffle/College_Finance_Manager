#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pytest
import pandas as pd
from functions import*


# In[12]:


def test_weeks_till_bankrupt():
    assert callable(weeks_till_bankrupt)
    ds = pd.read_excel('Expense_Python.xlsx')
    dk = pd.read_excel('Expense_Python2.xlsx')
    # Following code tests were taken from https://stackoverflow.com/questions/19917545/comparing-two-pandas-dataframes-for-differences and https://stackoverflow.com/questions/27950891/how-to-use-a-pandas-data-frame-in-a-unit-test
    try:
        pd.testing.assert_frame_equal(weeks_till_bankrupt(ds), weeks_till_bankrupt(dk))
        pd.testing.assert_series_equal(weeks_till_bankrupt(ds), weeks_till_bankrupt(dk))
        return True
    except:
        print('Dataframes are both different from each other!')
        


# In[11]:


def test_modify_columns():
    assert callable(modify_columns)
    ds = pd.read_excel('Expense_Python.xlsx')
    dk = pd.read_excel('Expense_Python2.xlsx')
    #Following code tests were taken from https://stackoverflow.com/questions/19917545/comparing-two-pandas-dataframes-for-differences and https://stackoverflow.com/questions/27950891/how-to-use-a-pandas-data-frame-in-a-unit-test 
    try:
        pd.testing.assert_frame_equal(modify_columns(ds), modify_columns(dk))
        pd.testing.assert_series_equal(modify_columns(ds), modify_columns(dk))
        return True
    except:
        print('Dataframes are both different from each other!')
    


# In[ ]:




