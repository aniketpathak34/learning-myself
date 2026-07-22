from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value}")
        return value
    return wrapper

@log_call
def add(a,b):
    return a+b

print(add.__name__)

# add(10, 20)
print("result:", add(10, 20))