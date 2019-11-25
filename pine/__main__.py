class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, x):
        self.stack.append(x)

    def ADD_TWO_VALUES(self):
        self.LOAD_VALUE(self.stack.pop() + self.stack.pop())

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def execute(self, code_object):
        instructions = code_object["bytecode"]
        numbers = code_object["numbers"]

        for (instruction, argument) in instructions:
            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(numbers[argument])
            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()


if __name__ == "__main__":
    code_object = {
        "bytecode": [
            ("LOAD_VALUE", 0),  # the first number
            ("LOAD_VALUE", 1),  # the second number
            ("ADD_TWO_VALUES", None),
            ("PRINT_ANSWER", None),
        ],
        "numbers": [4, 2],
    }

    pine = Interpreter()
    pine.execute(code_object)
