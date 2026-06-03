# main.py
import utils.calculator as calc

if __name__ == "__main__":
    print(f"Addition: {calc.add(5, 2)}")
    print(f"Subtraction: {calc.subtract(5, 2)}")
    print(f"Multiplication: {calc.multiply(5, 2)}")
    print(f"Division: {calc.division(5, 2)}")
else:
    print("Nothing to show")