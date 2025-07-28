# ANA's Smart Calculator  - Day 1 Project
# Built July 27, 2025
# Handles +,-,*,/ with input validation

if __name__ == "__main__":
    print("Welcome to ANA's Smart Calculator!")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator. Please use +, -, *, or /.")

            print(f"The result is: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using ANA's Smart Calculator!")
            break


        