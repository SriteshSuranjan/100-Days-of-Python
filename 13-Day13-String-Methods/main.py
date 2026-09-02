# Strings are immutable in Python, meaning that once a string is created, it cannot be changed. However, you can create new strings based on existing ones using various string methods.

a = "!!!Harry!! !!!!!!!!! Harry!!!"

print(len(a))  # Prints the length of the string

print(a.upper())  # Converts the string to uppercase
print(a.lower())  # Converts the string to lowercase

print(a.rstrip("!"))  # Removes trailing exclamation marks from the right side of the string

print(a.replace("Harry", "Ron"))  # Replaces occurrences of "Harry" with "Ron"

print(a.split(" "))  # Splits the string into a list of substrings based on spaces

blogHeading = "introduction tO Python"
print(blogHeading.capitalize())  # Converts the first character to uppercase and the rest to lowercase

str1 = "Welcome to the Console !!!"
print(str1.center(50)) # Centers the string within a field of 50 characters, padding with spaces on both sides
print(len(str1))  # Prints the length of the string
print(len(str1.center(50))) # Prints the length of the centered string, which will be 50

print(a.count("Harry"))  # Counts the number of occurrences of "Harry" in the string

print(str1.endswith("!!!"))  # Checks if the string ends with "!!!" and returns True or False

str1 = "Welcome to the Console !!!" # Variables can be overridden with new values, so we can reassign str1 to a new string
print(str1.endswith("to", 4, 10)) # Checks if the substring from index 4 to 10 ends with "to" and returns True or False

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # Finds the first occurrence of the substring "is" in the string and returns its index. If not found, it returns -1.
print(str1.find("ishh")) # Finds the first occurrence of the substring "ishh" in the string and returns its index. If not found, it returns -1.
# print(str1.index("ishh")) # Similar to find(), but raises a ValueError if the substring is not found.

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # Checks if all characters in the string are alphanumeric (letters and numbers) and returns True or False

str1 = "Welcome00"
print(str1.isalpha()) # Checks if all characters in the string are alphabetic (letters only) and returns True or False

str1 = "hello world"
print(str1.islower()) # Checks if all characters in the string are lowercase and returns True or False

str1 = "We wish you a Merry Christmas\n"
print(str1) 
print(str1.isprintable()) # Checks if all characters in the string are printable (not control characters) and returns True or False

str1 = "        "       #using Spacebar
print(str1.isspace()) # Checks if all characters in the string are whitespace (spaces, tabs, newlines) and returns True or False
str2 = "        "       #using Tab
print(str2.isspace()) # Checks if all characters in the string are whitespace (spaces, tabs, newlines) and returns True or False

str1 = "World Health Organization" 
print(str1.istitle()) # Checks if the string is in title case (each word starts with an uppercase letter followed by lowercase letters) and returns True or False
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) # Checks if all characters in the string are uppercase and returns True or False

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) # Checks if the string starts with "Python" and returns True or False

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) # Swaps the case of each character in the string (uppercase becomes lowercase and vice versa) and returns the new string

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title()) # Converts the string to title case (each word starts with an uppercase letter followed by lowercase letters) and returns the new string
