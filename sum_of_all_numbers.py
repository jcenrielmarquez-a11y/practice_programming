numbers = []

for i in range (10):
    num = int(input(f"Enter Number {i+1}: "))
    numbers.append(num)

total = sum(numbers)
print("The sum of all numbers is: ", total)