import time

def decorator_cach(fn):
    result = {}
    def wrapper(value1, value2):
        key = f"{value1}, {value2}"
        if key not in result.keys():
            print("add in dict")
            result[key] = fn(value1, value2)
        else:
            print("input from dict")
        return result[key]
    return wrapper

class Calc:
    @staticmethod
    @decorator_cach
    def plus(value_1, value_2):
        time.sleep(10)
        return value_1 + value_2

    def minus(self, value_1, value_2):
        return value_1 - value_2

    def multiplication(self, value_1, value_2):
        return value_1 * value_2

    def div(self, value_1, value_2):
        return value_1 / value_2


print(Calc.plus(2, 3))
print(Calc.plus(3, 10))
print(Calc.plus(2, 3))
print(Calc.plus(2, 1))
