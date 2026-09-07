def func1():
    try:
        l = [1, 5, 6, 7]
        num = int(input("Enter an index: "))
        print(l[num])
        return 1
    except:
        print("Error Occurred.")
        return 0
    # print("I am always executed") # Will not run if there will be errors.
    finally:
        print("This block is always executed.")
    
x = func1()
print(x)