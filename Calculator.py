def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def main():
    while True:
        print("MY Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option")

        if choice == '5':
            print("Goodbye!")
            break  

        if choice not in {'1', '2', '3', '4'}:
            print("Invalid option. Please try again.")
            continue

        try:
            num1 = int(input("Enter number: "))
            num2 = int(input("Enter number: "))
        except ValueError:
            print("Invalid number input. Try again.")
            continue

        if choice == '1':
            result = add(num1, num2)
            op = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op = '/'

        print(f"Result: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
