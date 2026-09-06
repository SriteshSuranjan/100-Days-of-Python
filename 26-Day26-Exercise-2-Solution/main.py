# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. 

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
# print(hour)
# minute = int(time.strftime('%M'))
# print(minute)
# second = int(time.strftime('%S'))
# print(second)

if(hour >= 5 and hour < 12):
    print("Good Morning Sir.")
if(hour >= 12 and hour < 17):
    print("Good Afternoon Sir.")
if(hour >= 17 and hour < 21):
    print("Good Evening Sir.")