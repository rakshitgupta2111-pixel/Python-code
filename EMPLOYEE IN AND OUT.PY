class Employee:

    def _init_(self):
        print("Employee created")

    def _del_(self):
        print("Destructor called")

def create_obj():
    print("Making object")
    obj=Employee()
    print("Function end")
    return obj

print("Calling create_obj() function")
obj=create_obj()
print("program end")