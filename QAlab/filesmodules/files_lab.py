
# import csv

# companies = []
# sales = []

# with open..... as ...:
#     read with csv.reader(alias)
#     next() - can skip over first line
#     for loop to iterate through each line:
#         append to companies
#         append to sales

# monthly sum = [list comprehension - use zip(*sales) - to unpack data] 

# yearly_sum = {}
# for loop to add companies as keys and sum of sales to values
    
# figure out a nice way to print out the results

import csv

companies = []
sales = []

with open("output.csv") as file:
    readFile = csv.reader(file)
    for i in readFile:
        companies.append(str(i[0]))
        sales.append([int(sale.replace(",", "")) for sale in i[1:]])

monthly_sales = [sum(month) for month in zip(*sales)]

yearly_sales = {company: sum(sale) for company, sale in zip(companies, sales)}

print("Sum of cars sold in each month:")
for i in range(len(monthly_sales)):
    print("Month", i + 1, ":", monthly_sales[i])
print("Total yearly sales by each manufacturer:")
for i in range(len(companies)):
    print(companies[i], ":", yearly_sales[companies[i]])