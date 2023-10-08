def calculate_root(number, root):
    return number ** (1/root)

while True:
    print("Welcome to the calculator")
    print("To collect 1")
    print("For subtraction 2")
    print("For multiplication 3")
    print("For division 4")
    print("For carrots 5")
    print("To exit 6")

    choice = input("select an operation: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("enter the first number: "))
        num2 = float(input("enter the second number: "))
        if choice == '1':
            print(num1 + num2)
        elif choice == '2':
            print(num1 - num2)
        elif choice == '3':
            print(num1 * num2)
        elif choice == '4':
            print(num1 / num2)

    elif choice == '5':
        number = float(input("enter the number: "))
        root = float(input("enter the root number: "))
        result = calculate_root(number, root)
        print(result)
    elif choice == '6':
        print("We await your next visit.")
        break
    else:
        print("Please choose a valid option")
