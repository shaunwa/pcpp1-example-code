import random

def retry(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries): 
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
            
            raise Exception('Max number of retries was reached!')
        
        return wrapper
    
    return decorator

@retry(max_retries=2)
def error_prone_func():
    should_fail = random.randint(0, 10)

    if should_fail < 9:
        raise Exception('Something bad happened!')
    
    print('Function completed successfully!')
    return 'Success!'

error_prone_func()