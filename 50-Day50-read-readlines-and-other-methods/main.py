# readliness() method
f = open('myfile.txt','r')
while(True):
    line = f.readline()
    if not line:
        break
    print(line)

# writeliness() method
g = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
g.writelines(lines)
g.close()

# split() method
h = open('myfile3.txt','r')
i = 0
while(True):
    i = i + 1
    line = h.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of Student{i} in Maths is: {m1}")
    print(f"Marks of Student{i} in Science is: {m2}")
    print(f"Marks of Student{i} in English is: {m3}")
    print(line)