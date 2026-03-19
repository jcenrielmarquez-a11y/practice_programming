numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Numbers with duplicates:", duplicates)
