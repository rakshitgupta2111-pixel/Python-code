try:
    number=int(input("Enter the number"))
    print("The number entered is: " , number)
except ValueError as ex:
    print("Exceptions:", ex)

try:
    num1,num2=eval(input("Enter two numbers separated by comma:"))
    result=num1/num2
    print("Result is: " , result)
except ZeroDivisionError:
    print("Division by zero is an error")
except SyntaxError:
    print("Comma is missing. Enter numbers using comma")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("This will execute no matter what")