def addition(a, b):
  return a + b

def subtraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

def main():
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  operation = input("Type your operation via it's corresponding number without the period: ")
  a = int(input("Type your first number: "))
  b = int(input("Type your second number: "))

  if operation == "1":
    print(addition(a, b))
  elif operation == "2":
    print(subtraction(a, b))
  elif operation == "3":
    print(multiplication(a, b))
  elif operation == "4":
    print(division(a, b))
  else:
    print("User input error. Try again")

main()
