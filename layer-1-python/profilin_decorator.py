import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return value
    return wrapper


@timer
def slow_add(a, b):
    time.sleep(1)
    return a+b


print(slow_add(10, 20))
print(slow_add(a=10, b=20))
print(slow_add.__name__)