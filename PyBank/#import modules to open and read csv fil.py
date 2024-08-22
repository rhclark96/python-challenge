#import modules to open and read csv files, statistics
import os
import csv
import statistics

#set path to csv
bank_path = os.path.join ("python-challenge","PyBank", "Resources", "budget_data.csv")

  #set initial value for a variable to count months 
month_count = 0

#set initial value for total
net_total = 0

#set initial value for "previous_row"
prev_row = 1088983

#set initial value for change 
one_change = 0

#list of change values, profit and months
profit_changes = []
month_of_change = []

#greatest values 
great_max = ["",0]
great_min = ["", 0]

#read file 
with open(bank_path, encoding='UTF-8') as bank_file:
    bankread = csv.reader(bank_file, delimiter=",")

    #print rows to check functionality, comment out
    #for row in bankread:
       # print (row)
    
    #skip header row 
    bank_header = next(bankread)

    
    for row in bankread:
        #loop through 1st column to count months
        month_count += 1
        # print month count to check functionality, comment out
        # print(f"Total Months: {month_count}")

        #loop through profit column to find total sum
        net_total += round(float(row[1]))
        #print total to check functionality, comment out
        #print (round(net_total))

        #loop through profit column comparing previoujs row to current row and subtracting to find change each month 
        one_change = int(row[1]) - int(prev_row)

        #add each individual change to the list of changes
        profit_changes += [one_change]
        #add the month of change to list of months (for later use when finding month of greatest min/max)
        month_of_change += row[0]
        #set current row to be the next "previous row"
        prev_row = int(row[1])
      
        #loop through changes as they are added to list, if greater than current value of great max then replace great max with change value
        if one_change > great_max[1]:
            great_max[0] = row[0]
            great_max[1] = one_change
        #print max value to check functionality, comment out later    
        #print (great_max)

        #loop through changes as they are added to list, if less than current value of great min then replace great min with change value 
        if one_change < great_min[1]:
            great_min[0] =row[0]
            great_min[1] = one_change
        #print to check functionality, comment out later
        #print(great_min)


#find the sum of all changes in the list
total_change = round(sum(profit_changes),2)
#print to check functionality, comment out later
#print(total_change)
#find the average change (total change divide by number of months -1, since there is 1 less change than there are total months)
avg_change = round(total_change/(month_count-1),2)
#print to check functionality, comment out later
#print(avg_change)

#print all values in desired format
print("Financial Analysis")

print("----------------------------")

print(f"Total Months: {month_count}")

print(f"Total: ${net_total}")

print(f"Average Change: ${avg_change}")

print(f"Greatest Increase in Profits: {great_max[0]} (${great_max[1]})")

print(f"Greatest Decrease in Profits: {great_min[0]} (${great_min[1]})")