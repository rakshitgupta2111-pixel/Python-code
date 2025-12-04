import keyword
a=5
b=2.8
c="Rakshit"
d=False
e="9"

print("Before typecasting")
print("The type a is:" , type(a))
print("The type b is:" , type(b))
print("The type c is:" , type(c))
print("The type d is:" , type(d))
print("The type e is:" , type(e))

a=float(a)
b=int(b)
c=bool(c)
d=str(d)
e=float(e)
print("After typecasting")
print("The type a is:" , type(a))
print("The type b is:" , type(b))
print("The type c is:" , type(c))
print("The type d is:" , type(d))
print("The type e is:" , type(e))
print("\n the keywords are:")
print(keyword.kwlist)
