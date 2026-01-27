def cube(num):
    return num**3 
num=int(input("Enter the number to be cubed:"))

def divide(num):
    if num%3==0:
        return cube(num)
    else:
        return False

print(divide(num))