# Shaik Fahad
# Oct 29, 2024

# Problem 3: This program calculate probabilty of heads 
import random
X = 84 

flips = 1000
results = []
for x in range(flips):
    if random.randint(1,100) <=x:
        results.append("heads")
    else:
        results.append("tails")

heads_count = results.count("heads")
heads_percentage = (heads_count / flips)*100

print(f"Heads appeared {heads_count} times out of {flips} flips.")
print(f"Percentage of heads: {heads_percentage:.2f}%")