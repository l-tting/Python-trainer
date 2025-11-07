basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

def get_gross_salary(basic,benefits):
    return basic + benefits

def get_nhif(gross):
    if gross >= 0 and gross <= 5999:
        nhif = 150
    elif gross >= 6000 and gross <= 7999:
        nhif = 300
    elif gross >= 8000 and gross <= 11999:
        nhif = 400
    elif gross >= 12000 and gross <= 14999:
        nhif = 500
    elif gross >= 15000 and gross <= 19999:
        nhif = 600
    elif gross >= 20000 and gross <= 24999:
        nhif = 750
    elif gross >= 25000 and gross <= 29999:
        nhif = 850
    elif gross >= 30000 and gross <= 34999:
        nhif = 900
    elif gross >= 35000 and gross <= 39999:
        nhif = 950
    elif gross >= 40000 and gross <= 44999:
        nhif = 1000
    elif gross >= 45000 and gross <= 49999:
        nhif = 1100
    elif gross >= 50000 and gross <= 59999:
        nhif = 1200
    elif gross >= 60000 and gross <= 69999:
        nhif = 1300
    elif gross >= 70000 and gross <= 79999:
        nhif = 1400
    elif gross >= 80000 and gross <= 89999:
        nhif = 1500
    elif gross >= 90000 and gross <= 99999:
        nhif = 1600
    else:
        nhif = 1700
    return nhif


def get_nssf(gross):
    if gross < 18000:
        nssf = gross * 0.06
    else:
        nssf = 1080
    return nssf


def get_nhdf(gross):
    return gross * 0.015


def get_taxable_income(gross,nssf,nhdf,nhif):
    return gross - (nssf + nhdf + nhif)


def get_payee(taxable_income):
    relief = 2400
    if taxable_income >=0 and taxable_income <= 24000:
        payee = 0
    elif taxable_income > 24000 and taxable_income <= 32333:
        payee = 2400 + ((taxable_income - 24000)*0.25) - relief
    elif taxable_income > 32333 and taxable_income <= 500000:
        payee = 2400 + (8333 * 0.25) + ((taxable_income - 32333)*0.3) - relief
    elif taxable_income > 500000 and taxable_income <= 800000:
        payee = 2400 + (8333 * 0.25) + (467667*0.3) + ((taxable_income - 500000) * 0.325) - relief
    else:
        payee = 2400 + (8333 * 0.25) + (467667*0.3) + (300000*0.325) + ((taxable_income - 800000) *0.35) - relief
    return payee


def get_net_salary(gross,nhif,nhdf,nssf,payee):
    return gross - (nhif + nhdf + nssf + payee)


gross_salary = get_gross_salary(basic_salary,benefits)
nhif = get_nhif(gross_salary)
nssf = get_nssf(gross_salary)
nhdf = get_nhdf(gross_salary)
taxable_income = get_taxable_income(gross_salary,nssf,nhdf,nhif)
payee = get_payee(taxable_income)
net_salary = get_net_salary(gross_salary,nhif,nhdf,nssf,payee)


print("-------------------------------------------------")
print("---------------MY TAX WORKFLOW-------------------")
print("Gross salary is Ksh. ",gross_salary)
print("NHIF is Ksh. ",nhif)
print("NSSF is Ksh. ",nssf)
print("NHDF is Ksh. ",nhdf)
print("Taxable income is Ksh. ",taxable_income)
print("Payee is Ksh. ",payee)
print("---------------------------------------------------")
print("Net salary is Ksh. ",net_salary)
print("----------------- end of tax -----------------------")


