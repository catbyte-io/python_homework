# Task 1: Writing and Testing a Decorator
import logging


# Set up logger
logger = logging.getLogger(__name__ + "parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# Define logging decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__} positional parameters: {args} keyword parameters: {kwargs} return: {result}")
    return wrapper


# Define function to use decorator
@logger_decorator
def meow():
    print("meow!")


# Define function that returns True
@logger_decorator
def true_func(*args):
    return True


# Define function that returns logging decorator
@logger_decorator
def log_dec(**kwargs):
    return logger_decorator


meow()
true_func(1, 2, 3)
log_dec(key1="a", key2="b", key3="c")
