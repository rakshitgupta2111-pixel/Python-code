choice=input ("Enter you want to calculate \n1.sum, \n 2.difference \n")
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2

if choice==1:
    print("sum is", add(num1,num2))
elif choice==2:
    print("Difference is", sub(num1,num2))