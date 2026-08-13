""""Decorator is function that takes function as argument returns the function, decorator is utilized when we dont want to change the existing function but add some extra things to it like greetings or authorization check authrntication cehck this kind of things"""

from functools import wraps

def log_call(func):
    # @wraps copies the original function's identity (__name__, __doc__) onto wrapper,
    # so add.__name__ stays "add" instead of becoming "wrapper"
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