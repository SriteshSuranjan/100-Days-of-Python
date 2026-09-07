ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep3 = {223: 64, 567: 97}

ep1.update(ep2)
print(ep1)

ep3.clear()
print(ep3)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.pop('eligible')
print(info)
info.popitem()
print(info)

info2 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info2['age']
print(info2)
# del info2
# print(info2) # NameError: name 'info' is not defined
