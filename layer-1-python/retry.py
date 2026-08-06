

def tryout(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
           try:
            return func(*args, **kwargs)
           except Exception as e:
              print(f"attempt {i+1} failed: {e}")
        print("all attempts failed")
    return wrapper

counter = {"n": 0}
@tryout
def flaky():
    counter['n'] += 1
    if counter['n'] <3:
        raise ValueError("network glitch")
    return "Connected"


print(flaky())