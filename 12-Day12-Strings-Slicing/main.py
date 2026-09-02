fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4])  # Prints "Mang" & include 0 but not 4
print(fruit[:4])  # Prints "Mang" & include 0 but not 4
print(fruit[1:4])  # Prints "ang" & include 1 but not 4
print(fruit[1:])  # Prints "ango" & include 1 but not 4
print(fruit[1:5])  # Prints "ango" & include 1 but not 5
print(fruit[:])  # Prints "Mango" & include 0 but not 5
print(fruit[0:-3])  # Prints "Ma" & include 0 but not 3
print(fruit[0:len(fruit)-3])  # Prints "Ma" & include 0 but not 3
print(fruit[-1:-3])  # 4:2 No sense, prints nothing
print(fruit[-3:-1])  # Prints "ng" & include -3 but not -1

# Quick Quiz: What will be the output of the following code?
nm = "Harry"
print(nm[-4:-2])  # Prints "ar" & include -4 but not -2