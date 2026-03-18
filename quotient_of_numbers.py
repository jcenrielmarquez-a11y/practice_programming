num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 != 0:
    quotient = num1 // num2
    print(f"The quotient of the two numbers is: ", quotient)
else:
    print("Division by zero is not allowed.")
