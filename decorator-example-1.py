import time

def watch_performance(func):
    total_time = 0
    number_of_executions = 0

    def wrapper(*args, **kwargs):
        nonlocal number_of_executions
        nonlocal total_time

        number_of_executions += 1

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        this_time = end - start
        print(f'{func.__name__} executed in {this_time} seconds')

        total_time += this_time
        average = total_time / number_of_executions

        print(f'The average execution time is: {average}')

        return result
    
    return wrapper

@watch_performance
def add(a, b):
    return a + b

@watch_performance
def wait_a_bit(seconds):
    time.sleep(seconds)

print(wait_a_bit(1))
print(wait_a_bit(2))
print(wait_a_bit(3))