import pytest
from pine import Interpreter

pine_interpreter = Interpreter()


class TestPineInterpreter:
    def test_basic_addition(self):
        code_object = {
            "instructions": [
                ("LOAD_VALUE", 0),  # the first number
                ("LOAD_VALUE", 1),  # the second number
                ("ADD_TWO_VALUES", None),
                ("PRINT_ANSWER", None),
            ],
            "numbers": [4, 2],
        }
        assert pine_interpreter.execute(code_object) == 6

    def test_variable(self):
        """>>> def s():
        ...     a = 1
        ...     b = 2
        ...     print(a + b)
        """
        code_object = {
            "instructions": [
                ("LOAD_VALUE", 0),
                ("STORE_NAME", 0),
                ("LOAD_VALUE", 1),
                ("STORE_NAME", 1),
                ("LOAD_NAME", 0),
                ("LOAD_NAME", 1),
                ("ADD_TWO_VALUES", None),
                ("PRINT_ANSWER", None),
            ],
            "numbers": [1, 2],
            "names": ["a", "b"],
        }

        assert pine_interpreter.execute(code_object) == 3
