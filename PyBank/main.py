import os
import csv

#################################################
def dict_stats(some_dict):
    print("Total Months: " + str(len(some_dict.keys())))
    
    total = 0
    change_monthly = 0
    change_rev_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_incr_date = ''
    greatest_decr_date = ''
    
    for key,value in some_dict.items():
        total = total + int(value)
        change_monthly = int(value) - change_monthly
        change_rev_total = change_rev_total + change_monthly
        
        if change_monthly >= greatest_increase:
            greatest_increase = change_monthly
            greatest_incr_date = key
        elif change_monthly <= greatest_decrease:
            greatest_decrease = change_monthly
            greatest_decr_date = key
        change_monthly = int(value)

    print('The revenue: ' + str(total))
    average_change = round((change_rev_total/len(some_dict.keys())), 2)
    print('Average Revenue Change:  $' + str(average_change))
    print('Greatest Increase in Revenue:  ' + greatest_incr_date + '  $' + str(greatest_increase) )
    print('Greatest Decrease in Revenue: ' + greatest_decr_date +  '  $' + str(greatest_decrease))
    
    # Set variable for output file
    output_file = os.path.join('Instructions/PyBank/raw_data',"output-file.txt")
    
    #  Open the output file
    with open(output_file, "a") as datafile:
        
        datafile.write('Financial Analysis' )
        datafile.write('\n' + '-----------------------------------------')
        datafile.write(('\n' + "Total Months: " + str(len(some_dict.keys()))))
        datafile.write('\n' + 'The revenue: ' + str(total))
        datafile.write('\n' + 'Average Revenue Change:  $' + str(average_change))
        datafile.write('\n' + 'Greatest Increase in Revenue:  ' + greatest_incr_date
                       + '  $' + str(greatest_increase) )
        datafile.write('\n' + 'Greatest Decrease in Revenue: ' + greatest_decr_date
                                      +  '  $' + str(greatest_decrease))
####################################################
new_dict2 = {}
budget2_path = os.path.join('Instructions/PyBank/raw_data', 'budget_data_2.csv')
with open(budget2_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        new_dict2[row[0]] = row[1]
print('Financial Analysis for budget_data_2.csv')
print('-----------------------------------------')
dict_stats(new_dict2)

new_dict1 = {}
budget1_path = os.path.join('Instructions/PyBank/raw_data', 'budget_data_1.csv')
with open(budget1_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        new_dict1[row[0]] = row[1]
dict_stats(new_dict1)
