# math_operations.py

import math

def getSquareRoot(x: int):
    return math.sqrt(x)

def getPower(x: int | float, y: int | float):
    return math.pow(x, y)

def getFloorValue(x: float):
    return math.floor(x)

def getFactorial(x: int):
    return math.factorial(x)

# Test block
if __name__ == "__main__":
    print(getSquareRoot(5))
    print(getPower(5, 3))
    print(getFloorValue(3.73))
    print(getFactorial(5))