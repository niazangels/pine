class Interpreter:
    def __init__(self):
        self.stack = []
        self.environment = {}

    def LOAD_VALUE(self, x):
        self.stack.append(x)

    def STORE_NAME(self, x):
        self.environment[x] = self.stack.pop()

    def LOAD_NAME(self, x):
        self.stack.append(self.environment[x])

    def ADD_TWO_VALUES(self):
        self.LOAD_VALUE(self.stack.pop() + self.stack.pop())

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def parse_argument(self, code_object, instruction, argument):
        if instruction in ["LOAD_VALUE"]:
            argument = code_object["numbers"][argument]
        elif instruction in ["LOAD_NAME", "STORE_NAME"]:
            argument = code_object["names"][argument]
        return argument

    def execute(self, code_object):
        instructions = code_object["instructions"]

        for (instruction, argument) in instructions:
            argument = self.parse_argument(code_object, instruction, argument)
            method = getattr(self, instruction)
            if argument is None:
                bytecode_method()
            else:
                bytecode_method(argument)
