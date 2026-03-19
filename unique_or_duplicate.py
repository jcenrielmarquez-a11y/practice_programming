numbers = []

while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input detected. Program terminated.")
        break

    num = int(user_input)
    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)
