class Cat:
    def __init__(self, name="Whiskey", age=2):
        self.name = name
        self.age = age

    def inspect(self):
        print(self.__dict__)

    ## Create a meow method
    def meow(self):
        print("meow")

class Cheshire(Cat):
    def __str__(self):
        return f"Cheshire Cat named {self.name} ({self.age} years old)"

    def meow(self):  # Override the meow method
        print("Meow and a Grin")

class Wonderland:
    def MadHatters():
        print("No Cat here. Mad Hatters")
    def QueenOfHearts ():
        print ("No Cat here. Queen Of Hearts")
    def Tree():
        print("Found the Cheshire Cat")
        return Cheshire()

# Create an instance of the Cat class
my_cat = Cat()
my_cat.inspect()  # Output: {'name': 'Whiskey', 'age': 2}
my_cat.meow()   # Output: "meow"
my_cheshire_cat = Cheshire() # creating an instance
print(my_cheshire_cat)  # printing Cheshire
my_cheshire_cat.meow()  # Output: "Meow and a Grin"
Wonderland.MadHatters()
Wonderland.QueenOfHearts()
my_wonderland_cat = Wonderland.Tree()
print(my_wonderland_cat)  # Output: Cheshire Cat named Whiskey (2 years old)
