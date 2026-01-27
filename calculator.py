class ScientificCalculator:
    # TODO: move last_result to a .txt to get a list of calculation results

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

    # Concise, but I want to do it by-hand in the future
    def power(self, input_number, power):
        self.last_result = input_number ** power
        return self.last_result

    # Placeholder until I can find a better way
    def square_root(self, input_number):
        self.last_result = input_number

        # Find square root by iterating up to half of the input number
        for multiple in range(input_number // 2):
            if multiple * multiple == input_number:
                self.last_result = multiple
                return self.last_result

        return self.last_result

    def variable_root(self, input_number, root):
        pass

    # Absolute value
    def absolute_of(self, input_number):
    #   Another way:
    #   return abs(input_number)

        if input_number < 0:
            # Invert to positive if the value is negative
            self.last_result = input_number * -1
        else:
            # If not negative, receive the value as-is
            self.last_result = input_number

        return self.last_result

    # Floor-dividing by 1 to return it rounded down
    def floor_of(self, input_number):
        self.last_result = input_number // 1
        return self.last_result

    # Same as above, but adding 1 to the floor-divided value to return it "rounded up"
    def ceiling_of(self, input_number):
        self.last_result = (input_number+1) // 1
        return self.last_result

    # Trigonomics
    def sine(self, input_number):
        # sin0: opposite / hypotenuse
        pass

    def cosine(self, input_number):
        # cos0: adjacent / hypotenuse
        pass

    def tangent(self, input_number):
        # tan0: opposite / adjacent
        pass

    # Others
    def get_pi(self):
        self.last_result = 3.14
        return self.last_result