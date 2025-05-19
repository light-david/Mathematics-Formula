"""
This program demonstrates the order of operations in Python.
The order of operations is important to understand when writing mathematical expressions.
The order of operations is as follows:
1. Parentheses
2. Exponents
3. Multiplication and Division (from left to right)
4. Addition and Subtraction (from left to right)
This program will show how to use parentheses to change the order of operations.
"""

class OrderOfOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, expression):
        """
        Calculate the result of the given expression.
        :param expression: The mathematical expression to evaluate.
        :return: The result of the expression.
        """
        try:
            self.result = eval(expression)
            return self.result
        except Exception as e:
            return f"Error: {e}"
        
    def show_order_of_operations(self):
        """
        Show the order of operations using examples.
        """
        print("Order of Operations:")
        print("1. Parentheses: (2 + 3) * 4 = ", self.calculate("(2 + 3) * 4"))
        print("2. Exponents: 2 ** 3 + 1 = ", self.calculate("2 ** 3 + 1"))
        print("3. Multiplication and Division: 8 / 2 * 4 = ", self.calculate("8 / 2 * 4"))
        print("4. Addition and Subtraction: 5 - 3 + 2 = ", self.calculate("5 - 3 + 2"))
        print("5. Combined: (2 + 3) * 4 - 1 = ", self.calculate("(2 + 3) * 4 - 1"))
        print("6. Complex: 2 + 3 * (4 - 1) ** 2 / 5 = ", self.calculate("2 + 3 * (4 - 1) ** 2 / 5"))
        print("7. Nested: (2 + (3 * 4)) - 5 = ", self.calculate("(2 + (3 * 4)) - 5"))

if __name__ == "__main__":
    order_of_operations = OrderOfOperations()
    order_of_operations.show_order_of_operations()
    # Example of using the calculate method directly
    expression = "(2 + 3) * 4 - 1"
    result = order_of_operations.calculate(expression)
    print(f"Result of '{expression}' is: {result}")

"""This program demonstrates the order of operations in Python.
It shows how to use parentheses to change the order of operations.
The calculate method evaluates the expression and returns the result.
The show_order_of_operations method provides examples of the order of operations.
The program is designed to be run as a script.
The main function creates an instance of the OrderOfOperations class and calls the show_order_of_operations method.
The calculate method can be used to evaluate any mathematical expression.
The program handles exceptions that may occur during the evaluation of the expression.
The result is printed to the console.
The program is easy to understand and can be used as a reference for the order of operations in Python.
The program is designed to be simple and straightforward."""