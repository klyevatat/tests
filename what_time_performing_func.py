import time

def decorator_time(fn):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return fn(*args, **kwargs)
    return wrapper

@decorator_time
def time_perform():
    t = time.perf_counter()
    return t

print(time_perform())