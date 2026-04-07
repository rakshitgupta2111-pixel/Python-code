class dog:
     animal="dog"
    
     def __init__(self,breed,colour):
       self.breed=breed
       self.colour=colour

labrador=dog("labrador","black")
pub=dog("pub","brown")

print("labrador is a ", labrador.animal)
print("pub is a " , pub.animal)
print("{} is {} ".format(labrador.breed,labrador.colour))
print("{} is {} ".format(pub.breed,pub.colour))