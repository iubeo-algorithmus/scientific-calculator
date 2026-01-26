class ScientificCalculator:
    # All of these will be removed

    def __init__(self, input_number):
        self.last_result = input_number

    def get_last_result(self):
        return self.last_result

    # Basic arithmetics
    def sum(self, first_input, second_input):
        self.last_result = first_input + second_input
        return self.last_result

    def subtract(self, first_input, second_input):
        self.last_result = first_input - second_input
        return self.last_result

    def multiply(self, first_input, second_input):
        self.last_result = first_input * second_input
        return self.last_result

    def divide(self, first_input, second_input):
        self.last_result = first_input / second_input
        return self.last_result

    # Could be done better
    def power(self, input_number, power):
        self.last_result = input_number ** power
        return self.last_result

    # Placeholder until I can find a better way
    def square_root(self, input_number):
        self.last_result = input_number

        for multiple in range(input_number // 2):
            if multiple * multiple == input_number:
                self.last_result = multiple
                return self.last_result

        return self.last_result

    def variable_root(self, input_number, root):
        pass

    # Absolute value
    def absolute_of(self, input_number):
        pass

    # Rounding values
    def ceiling_of(self, input_number):
        self.last_result = (input_number+1) // 1
        return self.last_result

    def floor_of(self, input_number):
        self.last_result = input_number // 1
        return self.last_result

    # Trigonomics
    def sine(self, input_number):
        pass

    def cosine(self, input_number):
        pass

    def tangent(self, input_number):
        pass