# Function to double the input
# def double(x):
#   return x * 2

# Lambda function to double the input
double = lambda x: x * 2
# Lambda function to cube of the input
cube = lambda x: x * x * x
# Lambda function to average of the inputs
avg = lambda x, y, z: (x + y + z) / 3

# Function defined as an argument of a function
def apply(fx, value):
    return 6 + fx(value)

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(apply(cube, 2))