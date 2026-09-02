name = "Sritesh"
friend = "Jyoti"
anotherFriend = 'Rohit'
apple = '''He said, 
Hi Sritesh!
Hey! I am Good.
"I want to eat an apple." '''

print("Hello, " +name+ "!")
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7])  #Throws an error because the index is out of range

print("Let's use a for loop\n")
for character in apple:
    print(character)