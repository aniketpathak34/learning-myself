



def cache(func):
    cache_str = {}
    def wrapper(*args, **kwargs):
        if args[0] in cache_str:
            print("Not computing")
            return cache_str.get(args[0])
        else:
            print("computing")
            discount = func(*args, **kwargs)
            cache_str[args[0]] = discount
        return discount
    return wrapper

            
@cache
def discount_calculator(price):
    discount = 40
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

print(discount_calculator(100))
print(discount_calculator(100))
print(discount_calculator(100))
print(discount_calculator(0))
print(discount_calculator(0))