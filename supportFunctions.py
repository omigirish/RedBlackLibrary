import time

#  Wrapper function that calculates execution time of the function decorated with it
def trackExecutionTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Total Execution Time: {execution_time:.4f} seconds")
        return result
    return wrapper


