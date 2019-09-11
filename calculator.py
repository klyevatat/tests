import time

def decorator_cach(fn):
    time.sleep(2)
    def wrapper(*args):
        print("decorator")
        return fn(*args)
    return wrapper

class Calc:
    def __init__(self):
        pass
    @decorator_cach
    def plus(self, value_1, value_2):
        print("function")
        return value_1 + value_2

    def minus(self, value_1, value_2):
        return value_1 - value_2

    def multiplication(self, value_1, value_2):
        return value_1 * value_2

    def div(self, value_1, value_2):
        return value_1 / value_2



calculator = Calc()
print(calculator.plus(2, 3))
print('---------------')
print(calculator.plus(2, 3))