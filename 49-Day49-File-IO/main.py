# READING A FILE
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE
f = open('myfile2.txt', 'w')
f = open('myfile2.txt', 'w')
f.write('Hello, world!')
f.close()

# APPEND A FILE
with open('myfile.txt', 'a') as f:
  f.write(" Hey I am inside the myfile.txt.")

# READING A FILE
with open('myfile.txt', 'r'):
  f.read()