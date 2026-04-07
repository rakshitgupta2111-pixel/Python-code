class vehicle:

    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

class bus(vehicle):

     pass

obj=bus("volvo",80,50)
print(obj.name,obj.max_speed,obj.milage)
