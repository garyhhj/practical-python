# bounce.py
#
# Exercise 1.5

current_height = 100 #meter 
num_bounce = 0 

for i in range(10): 
    num_bounce += 1
    current_height *= 3/5
    print(num_bounce, round(current_height, 4))