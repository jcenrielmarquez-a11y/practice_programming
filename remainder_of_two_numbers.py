num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 != 0:
    remainder = num1 % num2
    print(f"The remainder when {num1} is divided by {num2} is: {remainder}")
else:
    print("Division by zero is not allowed.")
