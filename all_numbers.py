num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start = min(num1, num2)
end = max(num1, num2)

print(f"Numbers between {num1} and {num2} are:")

for i in range(start + 1, end):
    print(i)
