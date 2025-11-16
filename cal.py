
def subtraction():
    print(f"The Results {x - y}")
def addition():
    print(f"The Results {x + y}")
def division():
    try:
        print(f"The Results {x / y}")
    except ZeroDivisionError:
        print("Can't divide with zero")
def multiplication():
    print(f"The Results {x * y}")

while True:
    try:
        print("""
    1. ADDITION
    2. SUBTRACTION
    3. MULTIPLICATON
    4. DIVISION
    """)
        choice = int(input("Choose from 1:4 to perform action "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please choose 1-4")
            continue
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        else:
            print("Invalid choice")

        ask = input("Continue? Y/N ").lower()
        if ask == "n":
            break
    except ValueError:
        print("Invalid choice")