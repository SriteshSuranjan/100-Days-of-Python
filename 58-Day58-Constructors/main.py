# Default Constructor
class Details:
  def __init__(self):
    print("Animal Crab belongs to Crustaceans group")

obj1=Details()

# Parametrized Constructor
class Person:
    def __init__(self, name, occ):
        print("Hey! I am a Person.")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}.")
        
a = Person("Sritesh", "Developer")
a.info()
b = Person("Suranjan", "Engineer")
b.info()