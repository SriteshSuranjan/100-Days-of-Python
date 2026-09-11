class Person:
  name = "Sritesh"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Suranjan"
a.occupation = "Accountant"

b.name = "Supriya"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()