# Simple Calculator in Python

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ["1", "2", "3", "4"]:
        # Get input numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform calculation based on user choice
        if choice == "1":
            result = num1 + num2
            operation = "+"
        elif choice == "2":
            result = num1 - num2
            operation = "-"
        elif choice == "3":
            result = num1 * num2
            operation = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "/"

        # Display result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    
    else:
        print("Invalid choice! Please select a valid option.")

# Run the calculator
calculator()
