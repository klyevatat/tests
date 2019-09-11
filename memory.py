import psutil

mem = psutil.virtual_memory()[3]
def decorator_memory(fn):
    def wrapped():
        return fn() - mem
    return wrapped

@decorator_memory
def memory():
    return psutil.virtual_memory()[3]

print(memory())