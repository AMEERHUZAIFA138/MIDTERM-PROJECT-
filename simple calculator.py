#simple calculator
while True:
    try:
        # User input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
            continue

        print(f"Result: {result}")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero.")