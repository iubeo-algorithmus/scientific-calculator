class ScientificCalculator:
    def __init__(self, current_number):
        self.last_result = current_number

    def get_last_result(self):
        return self.last_result

    # Basic arithmetics
    def sum(self, n1, n2):
        self.last_result = n1 + n2
        return self.last_result

    def subtract(self, n1, n2):
        self.last_result = n1 - n2
        return self.last_result

    def multiply(self, n1, n2):
        self.last_result = n1 * n2
        return self.last_result

    def divide(self, n1, n2):
        self.last_result = n1 // n2
        return self.last_result

    # Placeholder until I can find a better way
    def square_root(self, num):
        for multiple in range(num // 2):
            if multiple * multiple == num:
                self.last_result = multiple
                return self.last_result
        return num

    def variable_root(self, num, root):
        pass

    # Could be done better
    def power(self, num, power):
        result = 1

        for i in range(power):
            result = result * num

        self.last_result = result
        return self.last_result

    # Absolute value

    # Trigonometrics