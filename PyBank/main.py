import os
import csv

budget_data = (os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv'))
with open(budget_data) as csvfile:
    
    # define csvreader. csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #create an empty list to receive profit/loss values
    Profit_Loss = []
    Month = []
    
    #go to first row of data after the header
    csv_header = next(csvreader)
    
    #create loop to get data after header row into separate lists
    for row in csvreader:
    
        #add profit/loss values to its list as integers
        Profit_Loss.append(int(row[1]))
        #add month values to its own list
        Month.append(row[0])
    
    #Print List to confirm
    #print(Month)

    #Find Total Profit Loss.  0 is the starting value in the list
    Profit_Loss_Tot = sum(Profit_Loss,0)
    #print(Profit_Loss_Tot)

    #Find number of months
    num_months = len(list(Profit_Loss))
    #print(num_months)

    #create empty list to store the monthly changes in profit/loss
    Change_Profit_Loss = []

    #calculate monthly changes 
    for x, y in zip(Profit_Loss[0::], Profit_Loss[1::]):
        Change_Profit_Loss.append(y-x) 
    
    #check that the changes are being calculated
    #print ("Profit Loss Changes: ", str(Change_Profit_Loss))
    
    #identify number of months in change list
    num_changes = len(list(Change_Profit_Loss))
    #print to check that number of changes is one less than number of months
    #print(num_changes)

    #Find Average Change in  Profit Loss
    Avg_Change = round(((sum(Change_Profit_Loss,0))/num_changes),2)
    #print average change to check it
    #print(Avg_Change)
    
        
    #create dictionary to associate original data with profit/loss changes list
    #first, add "NA"  to the beginning of the Change_Profit_Loss list - no change in the first month
    a = "--"
    Change_Profit_Loss.insert(0,a)
    
    #print list to confirm
    #print(Change_Profit_Loss)

    #find max and min values of change for integers:
    maxvalue = (max([i for i in Change_Profit_Loss if isinstance(i, int)]))
    #print to check
    #print (maxvalue)

    minvalue = (min([i for i in Change_Profit_Loss if isinstance(i, int)]))
    #print (minvalue)
     
    #create dictionary
    budget_dict = dict(zip(Month, Change_Profit_Loss))

    #print dictionary to confirm
    #print(budget_dict)

    #get key value associated with min and max

    key_min = list(budget_dict.keys())[list(budget_dict.values()).index(minvalue)]
    #print(key_min)

    key_max = list(budget_dict.keys())[list(budget_dict.values()).index(maxvalue)]
    #print(key_max)

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


    
    


