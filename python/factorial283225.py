#factorial
from math import factorial
def number(i):
    if i<0:
        return print("factorial no existe")
    result = 1
    for  i in range (1, i + 1):
        result *= i
    return result
number = -5
print(f"el factorial es {number} es {factorial(number)}")