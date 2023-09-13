
# Setup lists ready to populate later:
companies = []
sales = []

# Create file object to read from the car.csv file:
carSales = open("Python/car.csv")

for row in carSales:

    # Split row data on commas to help work with:
    parts = row.split(',')
    
    # Output the company name and append to the companies list:
    company = parts[0]    
    companies.append(company)    

    # Output the sales figures and append to the sales list:
    sale_numbers = [int(x) for x in parts[1:]]
    sales.append(sale_numbers)

# Output the two lists to ensure data has been captured correctly:
print("Companies:", companies)
print("Sales:", sales)

# We are now ready to perform the calculations:
