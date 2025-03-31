#this function shows profit is weak, medium or strong
def profit(yuzde):
    if (0<yuzde) and (yuzde<10):
        print("Weak")
    elif yuzde<50:
        print("Medium")
    else:
        print("Strong")
#this function calculate profit
def fv(amount,rate,month):
    fv=amount*((1+rate)**month)
    p=fv-amount
    yuzde=(p/fv)*100
    print("Amount: $ "+str(fv))
    print("Profit: $ "+str(p)+" = "+str(yuzde)+" %")
    profit(yuzde)
#this funtion ask the user initial amount,interest rate and num. of months
def prompt():
    amount=0
    rate=0
    month=0
    i=1
    #it takes at most 2 investor
    while i<3:
        print("Investor ",i)
        amount=float(input("Initial amount? "))
        rate=float(input("Interest  rate? "))
        month=float(input("Num. of months? "))
        i+=1
        fv(amount,rate,month)
    print("Have a nice day!")
    
prompt()


