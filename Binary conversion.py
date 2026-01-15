# Decimal to Binary using nested loops

num = int(input("Enter a decimal number: "))
binary = ""

while num > 0:
    temp = ""

    while remainder >= 0:
        temp = str(remainder)
        break
    remainder = num % 2
    binary = temp + binary
    num=num//2
    
print("Binary value is:", binary)




