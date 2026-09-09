x = 10 # global variable
print(x)

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable
  print(f"The local value of x is {x}")
  print(f"The local value of y is {y}")
  print("Hello World!")

print(f"The global value of x is {x}")
my_function()
print(x) # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

