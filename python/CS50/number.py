number = input("Provide a number: ")

if number.isdigit():
    number = int(number)
    if number > 0:
        print("The number is positive")
else:
    print("Please enter a digit")