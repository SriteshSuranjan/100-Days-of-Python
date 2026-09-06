tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))

# tuple1[0] = 10 # This will give an error because tuples are immutable

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

country = ("Spain", "Italy", "India", "England" , "Germany")
#            [0]      [1]      [2]  
# Positive Indexing   
print(country[0]) # Prints the first element
print(country[1]) # Prints the second element
print(country[2]) # Prints the third element
# Negative Indexing   
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3]) # Prints the third last element
print(country[-4]) # Prints the fourth last element

# Check for Item
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
    
# Range of Index
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
print(animals[1:8:3])

