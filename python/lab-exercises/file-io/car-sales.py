
companies = []
sales = []

car_sales_monthly_total = []
car_sales_company_total = []

# Create file object to read from the car.csv file:
car_sales = open("Python/car.csv")

# Loop each row in the through the file:
for row in car_sales:

    # Split row data on commas to help work with:
    data_split = row.split(',')
    
    # Output the company name and append to the companies list:
    company_name = data_split[0]    
    companies.append(company_name)    

    # Output the sales figures and append to the sales list:
    raw_sales_list = [int(x) for x in data_split[1:]]
    sales.append(raw_sales_list)

# Sum of cars sold in each month:
car_sales_monthly_total = [sum(x) for x in zip(*sales)]
print(car_sales_monthly_total)

# Total yearly sales by each manufacturer:
i = 0
for row in sales:
    car_sales_company_total.append(companies[i] + " - " + str(sum(row)))
    i += 1
print(car_sales_company_total)