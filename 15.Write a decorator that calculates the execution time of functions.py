from time import perf_counter
from functools import wraps


def time_calculation(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("Program execution time: ", run_time)
        return value
    return wrapper_decorator


@time_calculation
def counter(x):
    mynum = 0
    for i in range(x):
        mynum += 1


counter(1000)
