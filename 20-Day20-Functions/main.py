def calculateGmean(a, b):
    gmean = (a * b)/(a+b)
    print(gmean)
    
def isGreater(a, b):
    if(a > b):
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")

def isLesser(a, b):
    pass # Can Write later on when I want to write the logic

a = 9
b = 8
isGreater(a, b)
# isLesser(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 7
isGreater(c, d)
# isLesser(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)