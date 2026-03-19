numbers = []

while True:
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input detected. Program terminated.")
        break

if numbers:
    max_count = 0
    most_duplicate = None
    for n in numbers:
        count = numbers.count(n)
        if count > max_count:
            max_count = count
            most_duplicate = n

    if max_count > 1:
        print("Number with the most duplicates:", most_duplicate)
    else:
        print("No duplicates found.")
else:
    print("No valid numbers were entered.")
