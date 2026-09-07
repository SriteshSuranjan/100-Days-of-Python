info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing single values
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values
print(info.values())

# Accessing keys
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
for key in info.keys():
    print(f"The value corresponding to the key {key} is: {info[key]}")

# Accessing key-value pairs
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
for key, value in info.items():
    print(f"The value value corresponding to the key {key} is: {value}")
    