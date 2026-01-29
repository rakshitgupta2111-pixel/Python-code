def sub(a,b):
    return a-b


a=int(input("Enter the total bill: "))
b=int(input("Enter the amount paid: "))

if a>b:
    print("amount left to be paid is: ", a-b)
else:
    print("Thank you")
    pass
