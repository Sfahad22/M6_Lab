#Shaik Fahad
#Oct 29, 2024

# Problem number 1: This program generates 10 random integers. 

import random
rand_nums = []
for _ in range (10):
    num = random.randrange(25,35)  #36 is exclusive, so this generate number from 25 to 35
    rand_nums.append(num)
    print(num)
    print("list of random numbers: ", rand_nums)
