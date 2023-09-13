def getIncomeTax(salary):

    personal_allowance = 12570
    tax_percentage = 0

    # Obtain the tax percentage bracket based on the salary inputted:
    if salary >= personal_allowance and salary <= 34500:
        tax_percentage = 20
    elif salary >= 34501 and salary <= 150000:
        tax_percentage = 40
    elif salary >= 150001:
        tax_percentage = 45
    else:
        tax_percentage = 0

    # Ensure that the personal allowance is taken off of the salary inputted:
    if tax_percentage > 0:
        salary = salary - personal_allowance

    # Work out the taxable amount on of the salary inputted:
    taxable_amount = int(round(salary * (tax_percentage / 100.0), 2))

    # Return the taxable amount
    return taxable_amount

###########################################

print("The taxable amount you will pay on £12000 is - £" + str(getIncomeTax(12000)))  # -- 0%
print("The taxable amount you will pay on £28000 is - £" + str(getIncomeTax(28000)))  # -- 20%
print("The taxable amount you will pay on £35000 is - £" + str(getIncomeTax(35000)))  # -- 40%
print("The taxable amount you will pay on £150000 is - £" + str(getIncomeTax(150000))) # -- 40%
print("The taxable amount you will pay on £160000 is - £" + str(getIncomeTax(160000))) # -- 45%