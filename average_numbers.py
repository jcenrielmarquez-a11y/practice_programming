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
    average = sum(numbers) / len(numbers)
    print("Average of entered numbers:", average)
else:
    print("No valid numbers were entered.")
