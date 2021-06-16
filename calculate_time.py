from functools import wraps
import time
def calculate_time(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        '''this is a wrapper function.'''
        print(f'Executing {func.__name__} function.')
        t1 = time.time()
        return_value = func(*args,**kwargs)
        print(f'time taken to execute this code is {time.time()-t1} seconds.')
        return return_value
    return wrapper_func
------------------------------------------
@calculate_time
def func():
    '''this is a sample function.'''
    return 'this is a function'
print(func())
# -----------------output:
# Executing func function.
# time taken to execute this code is 0.0 seconds.
# this is a function
------------------------------------------
@calculate_time
def square_series(n):
    '''this is a square function.'''
    return [i**2 for i in range(n+1)]
square_series(9999999)
# -----------------output:
# Executing square_series function.
# time taken to execute this code is 1.838411808013916 seconds.
------------------------------------------
