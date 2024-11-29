# class - blueprint for creating objects - custom data type

# "PascalCase" - rather than "camelCase"
class Car:
    # Constructor - special method that sets up attibutes of a new instance
    # will be automatically called when a new intance is created
    def __init__(self, make, model): ## Constructor - special method that sets up attributes of a new instance
        # pass
        # print('Called __init__')
        # print(self)
        #create an attibute 'make' and copy the calue of the 'make' param into it
        self.make = make # dot notation - <object>.<attr/method>
        self.model = model
        #implicitly returns self
        
    def start(self):
        print(f'{self.make} {self.model} Started')


#Main
my_car = Car('Honda','Civic')#create a new instance of Car
#my_car is now an object of class 'Car'
your_car = Car('toyota', 'corolla')
print(my_car.__dict__) # __dict__ built in function to expose attributes and values from class object
# print(your_car)
my_car.start()
your_car.start()
