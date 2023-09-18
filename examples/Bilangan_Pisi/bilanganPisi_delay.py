import random

from hackgen import TestInputFormat, TestGenerator, Language


class Div64(TestInputFormat):
    def inputs(self, difficult_level: int) -> None:
        arr = ['0', '1']
        size = random.randint(1, 100)
        s = "".join([arr[random.randint(0, 1)] for i in range(size)])
        print(s)


input_format = Div64()

test_generator = TestGenerator(
    10, input_format, Language.cpp('div64'), "Div64")
test_generator.run()