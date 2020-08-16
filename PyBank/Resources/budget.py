import os
import csv


date = []
profit = []
monthly_change = []

total_profit = 0
count = 0
profitlosstotalchange = 0


budget_data.csv = os.path.join('..", "Resources", 'budget_data.csv')

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
  

    for row in csv_reader:

        date.append(row[0])

        profit.append(row{1})
        total_profit = total_profit + int(row[1])

        total_profit = profitlosstotalchange
        
        monthlist = len(dates)
       
        total = sum("profit_loss_change")
       
        avgerage = sum("total_profit")/len("count")
       
        increase = "profit_loss_change" = max(monthly_change)
       
        decease = "profit_loss_change" = min(monthly_change)

    
    print("Financial Analysis")

    print"----------------------------"

    print ("Total Months", + str[count])
    print ("Total Profit", + str[total])
    print ("Average Change", + [average])
    print ("Greates Increase in Profits", + str(increase + date)
    print ("Greatest Decrease in Profits", + str(decrese + date)


