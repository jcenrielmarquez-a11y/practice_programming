numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = numbers[0]

for i in range(1, 10):
    result -= numbers[i]

print(f"The result of the first number minus all the remaining numbers is: ", result)
