import time

def decorator_time(fn):
    def wrapper():
        time.sleep(2)
        return fn()
    return wrapper

@decorator_time
def time_perform():
    t = time.perf_counter()
    return t

print(time_perform())