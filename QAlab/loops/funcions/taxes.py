def getIncomeTax(salary):
    pa = 11850
    tb = 34500
    tb2 = 150000
    tax_rate1 = 0.2
    tax_rate2 = 0.4
    tax_rate3 = 0.45

    if salary <= pa:
        tax_amount = 0
    elif salary <= tb:
        taxable_amount = salary - pa
        tax_amount = taxable_amount * tax_rate1
    elif salary <= tb2:
        taxable_amount = salary - pa
        tax_amount = taxable_amount * tax_rate2
    else:
        taxable_amount = salary - pa
        tax_amount = taxable_amount * tax_rate3

    return tax_amount


salary = int(input("Enter the salary amount: "))
tax = getIncomeTax(salary)
print(f"The income tax for a salary of £{salary} tax is £{tax}")
