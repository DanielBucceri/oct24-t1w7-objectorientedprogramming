# encaspulation, inhertience, polymorphism, ?? 

# class - blueprint for creating objects - custom data type

# "PascalCase" - rather than "camelCase"
class Car:
    # Constructor - special method that sets up attibutes of a new instance
    # will be automatically called when a new intance is created
    def __init__(self, make, model, engine): ## Constructor - special method that sets up attributes of a new instance
       # dunder __ makes attribute private
        #create an attibute 'make' and copy the calue of the 'make' param into it
        self.__make = make # dot notation - <object>.<attr/method>
        self.model = model
        self.engine = engine
        #implicitly returns self

    def start(self):
        print(f'{self.__make} {self.model} Started')
        
        

    # def display(self):
    #     print(f"this is a {self.make} {self.model}")
    def __str__(self):# returns string representation of object
       return f"this is a {self.__make} {self.model}"

   #getter
    def get_make(self): #retruieves current value of "__make" but keep private
     return self.__make
     #side-effects
 
    #setter 
    def set_make(self, new_make):
        # validate new_make values passed in
        # authorization as well.
        self.__make = new_make
        
        
#inheritence - "is a " relationship. as below petrol car IS A "car"
class PetrolCar(Car): # inherit Car class - Car is parent or superclass of PetrolCar
    def __init__(self, make, model, engine, tank_capacity_l): # redefining init to overwrite it
        super().__init__(make, model, engine) #gets superclass attributes from init_ otherwise not accessible becuase in new car class it overwrites the init causing attributes not to be defines
        self.tank_capacity_l = tank_capacity_l

    def __str__(self):
        return f'{super().__str__()}. it has a {self.tank_capacity_l}L tank' # {super().__str__()}

class Engine:
    def __init__(self, type, max_power_kw):
        self.type = type
        self.max_power_kw = max_power_kw
    def __str__(self):
        return f"This is a {self.type} engine with a maximum power of {self.max_power_kw} kW"


#Main
# composition - "has a" relationship. car HAS A "engine"
engine1 = Engine(type="petrol", max_power_kw=235)
# my_car = Car('Honda','Civic')#create a new instance of Car
#my_car is now an object of class 'Car'
# your_car = Car('toyota', 'corolla')
# print(my_car.__dict__) # __dict__ built in function to expose attributes and values from class object
# print(your_car)
# my_car.start()
# your_car.start()
# print(my_car.__make) # python defaults to making attributes public. accessible with my_car.make
# print(your_car)
# print(my_car.get_make())
# print("-----------------")


new_car = PetrolCar(make='Kia', model='Cerato', tank_capacity_l=47, engine=engine1)
# print(my_car.model)
# print(my_car.get_make()) # use  getter method to get private attr
print(new_car)








