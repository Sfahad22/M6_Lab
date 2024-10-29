# Shaik Fahad
# Oct 29, 2024

# Problem number 4: This program calculate factoria in two ways.

import math
num = int(input("Enter a number to calculate its factorial: "))

factorial_math = math.factorial(num)

factorial_loop = 1
for i in range(1, num +1):
    factorial_loop *= i
print(f"Factorial using math module: {factorial_math}")
print(f"Factorial using for loop: {factorial_loop}")

if factorial_math == factorial_loop:
    print("Both methods give the same result")
else:
    print("The result differ.")