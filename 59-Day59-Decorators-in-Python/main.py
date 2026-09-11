def greet(fx):
    # def mfx():
    def mfx(*args, **kwargs):
        # *args: As many arguments are there to be taken as tuple
        # **kwargs: As many arguments are there to be taken as dictonaries
        print("Good Morning!")
        # fx()
        fx(*args, **kwargs)
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("Hello World!")

@greet
def add(a, b):
    print(a + b)

# greet(hello)()
hello()
add(7, 5)