companies = []
sales = []
monthly_total = []
company_total = []

# Create file object to read from the car.csv file:
car_sales_object = open("Python/car.csv")
car_sales_data = car_sales_object.readlines()

# Loop each row in the through the file:
for row in car_sales_data:
    # Split row data on commas to help work with:
    data_split = row.split(',')
    # Output the company name and append to the companies list:
    company_name = data_split[0]    
    companies.append(company_name)    
    # Output the sales figures and append to the sales list:
    sales_line = []
    for x in data_split[1:]:
        sales_line.append(x)
    sales_line = list(map(int,sales_line))
    sales.append(sales_line)

print(companies)
print(sales)

# Sum of cars sold in each month:


# Total yearly sales by each manufacturer:
i = 0
for row in sales:
    company_total.append(companies[i] + " - " + str(sum(row)))
    i += 1

print(company_total)