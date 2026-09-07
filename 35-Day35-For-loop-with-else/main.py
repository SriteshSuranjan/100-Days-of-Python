for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Out of loop")
    
y = 0
while y < 7:
    print(y)
    y = y+1
    # if y == 4:
    #     break
else:
    print("Out of loop")