import math

class Calculator:
    def __init__(self):
        self.memory = 0
    
    def add(self, x, y):
        """Addition operation"""
        return x + y
    
    def subtract(self, x, y):
        """Subtraction operation"""
        return x - y
    
    def multiply(self, x, y):
        """Multiplication operation"""
        return x * y
    
    def divide(self, x, y):
        """Division operation with error handling"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def power(self, x, y):
        """Exponentiation operation"""
        return x ** y
    
    def square_root(self, x):
        """Square root operation"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(x)
    
    def factorial(self, x):
        """Factorial operation"""
        return math.factorial(int(x))
    
    def sine(self, x):
        """Sine function (input in degrees)"""
        return math.sin(math.radians(x))
    
    def cosine(self, x):
        """Cosine function (input in degrees)"""
        return math.cos(math.radians(x))
    
    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        return f"Stored {value} in memory"
    
    def recall_memory(self):
        """Recall value from memory"""
        return self.memory
    
    def clear_memory(self):
        """Clear memory"""
        self.memory = 0
        return "Memory cleared"

def main():
    calculator = Calculator()
    
    while True:
        print("\n--- Advanced Calculator ---")
        print("Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Sine")
        print("9. Cosine")
        print("10. Memory Store")
        print("11. Memory Recall")
        print("12. Clear Memory")
        print("0. Exit")
        
        choice = input("Enter operation number: ")
        
        try:
            if choice == '0':
                print("Thank you for using the calculator!")
                break
            
            if choice in ['1', '2', '3', '4', '5']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if choice == '1':
                    result = calculator.add(x, y)
                elif choice == '2':
                    result = calculator.subtract(x, y)
                elif choice == '3':
                    result = calculator.multiply(x, y)
                elif choice == '4':
                    result = calculator.divide(x, y)
                elif choice == '5':
                    result = calculator.power(x, y)
                
                print(f"Result: {result}")
            
            elif choice in ['6', '7', '8', '9']:
                x = float(input("Enter number: "))
                
                if choice == '6':
                    result = calculator.square_root(x)
                elif choice == '7':
                    result = calculator.factorial(x)
                elif choice == '8':
                    result = calculator.sine(x)
                elif choice == '9':
                    result = calculator.cosine(x)
                
                print(f"Result: {result}")
            
            elif choice == '10':
                value = float(input("Enter value to store: "))
                print(calculator.store_memory(value))
            
            elif choice == '11':
                print(f"Stored Value: {calculator.recall_memory()}")
            
            elif choice == '12':
                print(calculator.clear_memory())
            
            else:
                print("Invalid operation. Please try again.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
