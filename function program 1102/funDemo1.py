def calcTax(amount, taxRate):# amount = 100, taxRate = 0.05
    tax = amount * taxRate     # tax is local variable
    return tax                # return is necessary; it returns tax to the caller

def main():
    myAmount = float(input("please enter the amount: "))
    myRate = float(input("please enter the tax rate: "))
    theTax= calcTax(myAmount, myRate)    # tax is local variable
    print("Tax amount is: ", theTax)

main()