a = 4
b = "4"

print(a is b) # Compare the Exact location of object in memory
print(a == b) # Compare the Value

a1 = 4
b1 = 4

print(a1 is b1) # True Because It is a constant and it is immutable so, it will not waste another memory location
print(a1 == b1) # True


c = [1, 2, 3]
d = [1, 2, 3]

print(c == d)  # True
print(c is d)  # False

e = None
f = None
print(e is f) # True
print(e is None) # True
print(e == f) # True