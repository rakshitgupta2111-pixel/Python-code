a=input("Enter a word:")
for i in a:
    if i == 'a':
        print("A is found",i)
        break
    else:
        print("A is not found",i)

b=int(input("Enter a two digit large number:"))
if b%20==0:
    print("twist")
elif b%15==0:
    pass
elif b%5==0:
    print("fizz")
elif b%3==0:
    print("buzz")
else:
    print(b)

for i in range(10,0,-1):
    if i==5:
        continue
    print(i)