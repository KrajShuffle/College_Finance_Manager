# College_Finance_Manager
Currently, college students undergo many expenses over one week to satisfy their daily needs. The goal of this project is to create an easy-to-use module where users could import a spreadsheet of their expenses and run it to keep track of their expenses over one week. This project REQUIRES the imported excel spreadsheet to have purchases' amounts in the left-most column and the initial cash amount in the column to its right. Three methods were created in this project to revolutionize the original messy spreadsheet into a clean, reusable, and powerful dataframe object.

The first method cleans the original spreadsheet and relabels the original column labels to better column titles. The second method adds three new columns: 'Balance','Number of Items Purchased', and 'Total Expense From Last Week' with their respective values. Finally, the third method calculates how many weeks is the user safe from bankruptcy if he or she continues their current spending rate.

Requirements:
1. Must install xlrd. 
2. Must install pandas as pd. 
3. Both installations can be resolved via using code 'pip install (specific module's name)' in the terminal
