# Define a Class
class House:

    ## self does the same job as "this"
    ## arguments are any parameter after "self", in this case with a default value
    def __init__(self, model = "a"):
        self.square_feet = 1000
        self.bathrooms = 2
        if(model == "b"):
            self.bedrooms = 2
        else:
            self.bedrooms = 3

    ## Create an inspect method
    def inspect(self):
        print(self.__dict__)

# Instantiate an instance of the class
house = House()
house2 = House("b")

print(house) ## Print the type of object and it's memory
house.inspect()## Convert to Dictionary for printing purposes

print(house2) ## Print the type of object and it's memory
house2.inspect() ## Convert to Dictionary for printing purposes

'''
# Define a Class
class House:
    
    ## self does the same job as "this"
    ## arguments are any parameter after "self", in this case with a default value
    def __init__(self, model = "a"):
        self.square_feet = 1000
        self.bathrooms = 2
        if(model == "b"):
            self.bedrooms = 2
        else:
            self.bedrooms = 3
            
    ## Create an inspect method
    def inspect(self):
        print(self.__dict__)
        
class Duplex(House):
    
    def __init__(self, model):
        super().__init__(model) ## call parent constructor
        

# Instantiate an instance of the class
house = House()
house2 = House("b")

print(house) ## Print the type of object and it's memory
house.inspect()## Convert to Dictionary for printing purposes

print(house2) ## Print the type of object and it's memory
house2.inspect() ## Convert to Dictionary for printing purposes

duplex = Duplex("b")
print(duplex)
duplex.inspect()
'''

'''
# Define a Class
class House:
    
    number_of_houses = 0 ## Class Property for the Number of Houses
    
    ## self does the same job as "this"
    ## arguments are any parameter after "self", in this case with a default value
    def __init__(self, model = "a"):
        House.addHouse()
        self.square_feet = 1000
        self.bathrooms = 2
        if(model == "b"):
            self.bedrooms = 2
        else:
            self.bedrooms = 3
            
    ## Create an inspect method
    def inspect(self):
        print(self.__dict__)
        
    ## create a class method, cls replaces self and represent the class not the instance
    @classmethod
    def addHouse(cls):
        cls.number_of_houses += 1
    
        
class Duplex(House):
    
    def __init__(self, model):
        super().__init__(model) ## call parent constructor
        

# Instantiate an instance of the class
house = House()
house2 = House("b")

print(house) ## Print the type of object and it's memory
house.inspect()## Convert to Dictionary for printing purposes

print(house2) ## Print the type of object and it's memory
house2.inspect() ## Convert to Dictionary for printing purposes

duplex = Duplex("b")
print(duplex)
duplex.inspect()

## Printing a Class Property
print(House.number_of_houses)
'''