# Come Up with a Program that will store some Gross Salary in variable, Then Using If Else...Else if Statements Determine the Monthly Contribution Someone will Pay. 

GrossSalary = int(input("Enter Your Gross Salary: "))

if GrossSalary > 0 and GrossSalary < 5999:
    print("Ksh 150.00")
elif GrossSalary < 7999 and GrossSalary > 6000:
    print("Ksh 300.00")
elif GrossSalary < 11999 and GrossSalary > 8000:
    print("Ksh 400.00")
elif GrossSalary < 14999 and GrossSalary > 12000:
    print("Ksh 500.00")
elif GrossSalary < 19999 and GrossSalary > 15000:
    print("Ksh 600.00")
elif GrossSalary < 24999 and GrossSalary > 20000:
    print("Ksh 750.00")
elif GrossSalary < 29999 and GrossSalary > 25000:
    print("Ksh 850.00")
elif GrossSalary < 49999 and GrossSalary > 30000:
    print("Ksh 1000.00")
elif GrossSalary < 99999 and GrossSalary > 50000:
    print("Ksh 1500.00")
else:
    print("Ksh 2000.00")
