#import modules
import os
import csv

#point to csv file
csvpath = os.path.join('Resources','budget_data.csv')

#read in csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #ignore header
    csv_header = next(csvreader)

    #initialize variables
    month_count=0
    total=0
    revenue=[]
    change=[]
    date=[]

    #determine number of months, total, and create list of date and revenue columns
    for row in csvreader:
        month_count += 1
        total += int(row[1])
        revenue.append(float(row[1]))
        date.append(row[0])

    #substract the current revenue from previous to calculate change in revenue
    for i in range(1,len(revenue)):
        change.append(revenue[i]-revenue[i-1])

    #determine the greatest increase and greatest decrease in profits
    changebase_i=change[0]
    changebase_d=change[0]
    for j in range(1,len(change)):
        if change[j]>changebase_i:
            changebase_i=change[j]
            rowi=j
        if change[j]<changebase_d:
            changebase_d=change[j]
            rowd=j

    #grab the date associated with greatest increase and decrease
    for k in range(1,len(date)):
        if k == rowi + 1:
            datei=date[k]
        if k == rowd + 1:
            dated=date[k]

#print to terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {datei}: (${changebase_i})")
print(f"Greatest Decrease in Profits: {dated}: (${changebase_d})")

#print to csv
# Specify the file to write to
output_path = os.path.join("Output", "pybank_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f"Total Months: {month_count}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change: ${round(sum(change)/len(change),2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {datei}: (${changebase_i})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {dated}: (${changebase_d})"])