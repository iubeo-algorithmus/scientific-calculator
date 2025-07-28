class Calculator:

    # Basic arithmetic
    __add__ = '+'
    __sub__ = '-'
    __mul__ = '*'
    __truediv__ = '/'

    # Stores the last value used
    last_number: int = 0

    def self(self):
        return self

    def get_last_number(self) -> int:
        return self.last_number

    def add(self, num1, num2) -> int:
        self.last_number = num1 + num2
        return self.last_number

    def subtract(self, num1, num2) -> int:
        self.last_number = num1 - num2
        return self.last_number

    def multiply(self, num1, num2) -> int:
        self.last_number = num1 * num2
        return self.last_number

    def divide(self, num1, num2) -> int:
        self.last_number = num1 / num2
        return self.last_number
