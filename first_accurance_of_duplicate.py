numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

seen = set()
result = []
for n in numbers:
    if n not in seen:
        result.append(n)
        seen.add(n)

print("Numbers with duplicates removed (keeping first occurrence):", result)
