import os
import csv

budget_data = (os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv'))
with open(budget_data) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #create empty lists to receive values
    Profit_Loss = []
    Month = []
    Change_Profit_Loss = []

    #go to first row of data after the header
    csv_header = next(csvreader)
    
    #create loop to get data after header row into separate lists
    for row in csvreader:
    
        #add profit/loss values to its list as integers
        Profit_Loss.append(int(row[1]))
        #add month values to its own list
        Month.append(row[0])
    
        
    #Find Average Change in Profit Loss
    # first,calculate monthly changes and populate Change_Profit_Loss list using zip function
    for x, y in zip(Profit_Loss[0::], Profit_Loss[1::]):
        Change_Profit_Loss.append(y-x) 
        
    #identify number of months in change list
    num_changes = len(list(Change_Profit_Loss))
    Avg_Change = round(((sum(Change_Profit_Loss,0))/num_changes),2)
    
    #create dictionary to associate original data with profit/loss changes list
    #add "NA"  to the beginning of the Change_Profit_Loss list - no change in the first month
    a = "--"
    Change_Profit_Loss.insert(0,a)
    budget_dict = dict(zip(Month, Change_Profit_Loss))

    #find max and min values of change in Change_Profit_Loss list:
    maxvalue = (max([i for i in Change_Profit_Loss if isinstance(i, int)]))
    minvalue = (min([i for i in Change_Profit_Loss if isinstance(i, int)]))
        
    #get months (keys) associated with min and max profit/loss values from dictionary

    key_min = list(budget_dict.keys())[list(budget_dict.values()).index(minvalue)]
    key_max = list(budget_dict.keys())[list(budget_dict.values()).index(maxvalue)]
    
    
    #Find results for Total Profit Loss and Total number of months.  
    Profit_Loss_Tot = sum(Profit_Loss,0)
    num_months = len(list(Profit_Loss))
    
#apply formatting to monetary values: 
Profit_Loss_Tot = "${}".format(Profit_Loss_Tot)
Avg_Change = "${}".format(Avg_Change)
maxvalue = "${}".format(maxvalue)
minvalue = "${}".format(minvalue)  

#print results to terminal
print("Financial Analysis")
print("--------------------------")
print("Total Months = " + str(num_months))
print("Total Profit/Loss = " + str(Profit_Loss_Tot))
print("Average Change = " + str(Avg_Change))
print("Greatest Increase in Profits = " + str(key_max) + " ("+ (maxvalue) +")")
print("Greatest Decrease in Profits = " + str(key_min) + " ("+ (minvalue) +")")


#print results to textfile
with open(os.path.join('Analysis', 'Financial_Results.txt'), "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write("Total Months = " + str(num_months) + '\n')
    text_file.write("Total Profit/Loss = " + str(Profit_Loss_Tot) + '\n')
    text_file.write("Average Change = " + str(Avg_Change) + '\n')
    text_file.write("Greatest Increase in Profits = " + str(key_max) + " ("+ (maxvalue) +")\n")
    text_file.write("Greatest Decrease in Profits = " + str(key_min) + " ("+ (minvalue) +")\n")
    text_file.flush()
    text_file.close()


    
    


