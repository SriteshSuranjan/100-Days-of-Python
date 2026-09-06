countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
print(type(countries))
print(type(temp))
countries2 = ("Vietnam", "Ohio", "China")
southEastAsia = countries + countries2
print(southEastAsia)
print(type(southEastAsia))

# count() Method
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# index() Method
Tuple2 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple2.index(3)
print('Index of 3 in Tuple2 is:', res)