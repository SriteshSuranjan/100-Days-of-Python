def average(a, b, c = 1):
    print("The average is: ", (a + b + c) / 3)
average(4, 6) # Uses default value of c = 1
average(4, 6, 8) # Uses provided value of c = 8

# Default Arguments in Functions
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")

# Keyword Arguments in Functions
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Required Arguments in Functions
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
# name("Peter", "Quill") # This will raise an error because the required argument 'lname' is missing.
name("Peter", "Quill", "Ravager") # This will work correctly because all required arguments are provided.

# Variable-length Arguments in Functions
# Arbitrary Arguments in Functions
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")

def averages(*numbers):
    print(type(numbers)) # This will print <class 'tuple'> because the arbitrary arguments are stored in a tuple.
    sum = 0
    for i in numbers:
        sum += i
        print("The average is: ", sum / len(numbers))
averages(4, 6, 8, 10, 12)

# Keyword Arbitrary Arguments in Functions
def name(**name):
    print(type(name)) # This will print <class 'dict'> because the keyword arguments are stored in a dictionary.
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

# return Statement in Functions
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))
