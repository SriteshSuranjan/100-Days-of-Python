name = 'Abhishek'
for i in name:
    # print(i, end=", ")
    print(i)
    if(i == 'b'):
        print("This is something special.")

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:
        print(i)

print("Now printing numbers from 0 to 4")
for k in range(5):
    print(k)

print("Now printing numbers from 4 to 8")
for k in range(4,9):
    print(k)

print("Now printing numbers from 4 to 8 with a step of 2")
for k in range(4, 9, 2):
    print(k)
# range(start, stop, step)  # start is inclusive, stop is exclusive, step is the increment
