hours =float(input("please enter the number of hours: "))
pay_rate =float(input("please enter the hourly pay rate: "))
tax_p =float(input("please enter the tax percentage: "))
gross_pay = hours * pay_rate
net_pay = gross_pay - (gross_pay * tax_p / 100)
print ("the net pay is %f" %(net_pay))
