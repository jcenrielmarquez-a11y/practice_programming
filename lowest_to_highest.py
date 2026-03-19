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
    numbers.sort()
    print("Numbers from lowest to highest:", numbers)
else:
    print("No valid numbers were entered.")
