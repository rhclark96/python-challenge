#import modules to open and read csv files
import os
import csv

#set path to csv
bank_path = os.path.join ("python-challenge","PyBank", "Resources", "budget_data.csv")

  #set initial value for a variable to count months 
month_count = 0

#read file 
with open(bank_path, encoding='UTF-8') as bank_file:
    bankread = csv.reader(bank_file, delimiter=",")

    #print rows to check functionality, comment out
    #for row in bankread:
       # print (row)
    
    #skip header row 
    bank_header = next(bankread)

    #loop through rows to count months
    for row in bank_file:
        if row[0]: 
           month_count = month_count + 1
# print month count to check functionality, comment out
#print(f"Total Months: {month_count}")
