import os

import csv
    
csvpath = os.path.join('..', "PyBank", "budget_data.csv")

# set variable for calculations
count = 0
net_profit = 0
val1 = 0
val2 = 0
diff = 0
diff_total = 0
max_incr = 0
max_incr_mon = ''
max_decr = 0
max_decr_mon = ''

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
    
    # count the number of months
        count +=1
    # calculate net profits
        row[1] = int(row[1])
        net_profit += row[1]

    # cacluate the average of the changes in profits
        if diff == 0:
            val1 = row[1]
            diff = val1 - val2
            val2 = val1
        else:
            val1 = row[1]
            diff = val1 - val2
            diff_total += diff
            val2 = val1
    
    # calculate the greatest increase
        if row[1] > max_incr:
            max_incr = diff
            max_incr_mon = row[0]

    # calculate the greatest decrease
        if row[1] < max_decr:
            max_decr = diff
            max_decr_mon = row[0]

    avg_change = diff_total / (count -1)

    print("Finnancial Analysis")
    print("--------------------------")
    print("Total months:" , count)
    print("Total:" , net_profit)
    print("Average Change:", avg_change) 
    print("Greatest Increase in Profits:", max_incr_mon, max_incr)
    print("Greatest Decrease in Profits:", max_decr_mon, max_decr)
  
# create text for output 
output = ["Finnancial Analysis", "--------------------------", "Total months:" , count]

'''
output_path = os.path.join("..", "Pybank", "new.txt")

with open(output_path, 'w', newline='') as txtfile:

    output_path.writelines(output)
'''
