from calculator import Scientific_Calculator

calc = Scientific_Calculator(0)

num1 = 36
num2 = 2
power = 1

print(f"SUM TEST.\n"
      f"Num1: {num1}, Num2: {num2}\n"
      f"Result: {calc.sum(num1, num2) == 38}\n")

print(f"Last Result: {calc.get_last_result()}\n")

print(f"SUBTRACT TEST.\n"
      f"Num1: {num1}, Num2: {num2}\n"
      f"Result: {calc.subtract(num1, num2) == 34}\n")

print(f"Last Result: {calc.get_last_result()}\n")

print(f"MULTIPLY TEST.\n"
      f"Num1: {num1}, Num2: {num2}\n"
      f"Result: {calc.multiply(num1, num2) == 72}\n")

print(f"Last Result: {calc.get_last_result()}\n")

print(f"DIVIDE TEST.\n"
      f"Num1: {num1}, Num2: {num2}\n"
      f"Result: {calc.divide(num1, num2) == 18}\n")

print(f"Last Result: {calc.get_last_result()}\n")

print(f"SQUARE ROOT TEST.\n"
      f"Num: {num1}\n"
      f"Result: {calc.square_root(num1) == 6}\n")

print(f"Last Result: {calc.get_last_result()}\n")

print(f"POWER TEST.\n"
      f"Num: {num1}, Power: {power}\n"
      f"Result: {calc.power(num1, power) == 36}\n")

print(f"Last Result: {calc.get_last_result()}\n")