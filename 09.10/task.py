def cache(func):
    stored_results = {} 

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Результат взят из кеша")
            return stored_results[key]

        print("Вычисляем заново...")
        result = func(*args, **kwargs)
        stored_results[key] = result  
        return result

    return wrapper


import time

@cache
def slow_function(x, y):
    time.sleep(2)  
    return x ** y


print(slow_function(2, 10))  
print(slow_function(2, 10))  
print(slow_function(3, 5))  
