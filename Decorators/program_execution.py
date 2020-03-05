def decorator(func):
    import time
    from datetime import datetime
    def wrapper():
        start_time = time.time()
        start_processor_time = time.process_time()
        start_datetime = datetime.now()
        func()
        end_time = time.time()
        end_processor_time = time.process_time()
        end_datetime = datetime.now()
        print(func.__name__)
        print('Elapsed time: {}'.format(end_time - start_time))
        print('Process time: {}'.format(end_processor_time - start_processor_time))
        print('Duration: {}'.format(end_datetime - start_datetime))
        print()
    return wrapper

@decorator
def print_function():
    print("Function...")

print_function()

@decorator
def fetch_webpage():
    import requests
    # For Windows use pip install requests
    # OSX/Linux use $ sudo pip install requests
    webpage = requests.get('https://google.com')

fetch_webpage()