# union() and update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.union(cities2))
print(cities, cities2)
cities.update(cities2)
print(cities)
print(cities, cities2)

#intersection() and intersection_update()
cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities3.intersection(cities2))
print(cities3, cities2)
cities3.intersection_update(cities2)
print(cities3)
print(cities3, cities2)

# symmetric_difference and symmetric_difference_update
cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities4.symmetric_difference(cities2))
cities4.symmetric_difference_update(cities2)
print(cities4)

# difference() and difference_update()
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities6 = {"Seoul", "Kabul", "Delhi"}
print(cities5.difference(cities6))
print(cities6.difference(cities5))
cities5.difference_update(cities6)
print(cities5)

# isdisjoint()
cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities8 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities7.isdisjoint(cities8))

# issuperset()
cities9 = {"Seoul", "Kabul"}
print(cities7.issuperset(cities9))
cities10 = {"Seoul", "Madrid","Kabul"}
print(cities7.issuperset(cities10))

# issubset()
cities11 = {"Delhi", "Madrid"}
print(cities11.issubset(cities7))

# add()
cities11.add("Helsinki")
print(cities11)

# remove()/discard()
cities11.remove("Madrid")
print(cities11)
cities11.discard("Tokyo")
print(cities11)

# pop()
item = cities11.pop()
print(cities11)
print(item)

# del
del cities11
# print(cities11) # NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

# clear()
cities10.clear()
print(cities10)

# Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
