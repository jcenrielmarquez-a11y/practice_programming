numbers = []

while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input detected. Program terminated.")
        break

    num = int(user_input)
    numbers.append(num)

if numbers:
    print("Lowest number entered:", min(numbers))
else:
    print("No valid numbers were entered.")
