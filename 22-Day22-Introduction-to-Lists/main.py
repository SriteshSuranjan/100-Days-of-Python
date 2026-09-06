lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
print(type(lst1))
print(type(lst2))
print(lst1[0])
print(lst2[0])

marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[-1])
print(marks[-2])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
print(animals[3:7:2])	#using positive indexes with step
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes
print(animals[1:8:3]) #using positive indexes with step

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# List Comprehension
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
