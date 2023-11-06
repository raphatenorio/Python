import math
import os

last_result = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Shows the user what he can do
    print("Welcome to Python Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")
    print("6. Power to...")
    print("777. Memory")
    print("888. Clear Memory")
    print("999. Quit")
    choice = input("Choose what operation you want to do: ")
    # Conditional statments
    if choice == '999':
        print("See Ya!")
        os.system('cls')
        break

    elif choice == '777':
        if last_result == []:
            print('Nothing to print.')
        else:
            print(f'Last result: {last_result}')

    elif choice == '888':
        if last_result == []:
            print('Nothing to clear.')
        else:
            last_result.clear()
            print("Memory Cleared.")

    elif choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            result = num1 + num2
            print(f'{num1} + {num2} = {result}')
            last_result.append(result)
        elif choice == '2':
            result = num1 - num2
            print(f'{num1} - {num2} = {result}')
            last_result.append(result)
        elif choice == '3':
            result = num1 * num2
            print(f'{num1} * {num2} = {result}')
            last_result.append(result)
        elif choice == '4':
            if num2 == 0:
                print("You can't to that!")
            else:
                result = num1 / num2
                print(f'{num1} / {num2} = {result}')
                last_result.append(result)

    elif choice == '5':
        num1 = float(input("Enter a number: "))
        if num1 < 0:
            print('Please enter a positive number!')
        else:
            result = math.sqrt(num1)
            print(f'The Square root of {num1} is equal to: {result}')
            last_result.append(result)

    elif choice == '6':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("to the power of: "))
        result = math.pow(num1, num2)
        print(f'{num1} to the power of {num2} is equal to: {result}')
        last_result.append(result)

    else:
        print('Enter a valid command')
    input("Press Enter to continue...")
