print ("BASIC CALCULATOR")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sign = input("Enter the operation: ")

if sign == "+":
  print(num1 + num2)
elif sign == "-":
  print(num1 - num2)
elif sign == "*":
  print(num1 * num2)
elif sign == "/":
  print(num1 / num2)
else:
  print("Invalid operation")