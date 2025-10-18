# =====================================================
# PYTHON DECORATORS - NOTES WITH EXAMPLES
# =====================================================

# ---------------------------
# 1. BASIC FUNCTION DECORATOR
# ---------------------------

def my_decorator(func):
    # wrapper adds extra features around 'func'
    def wrapper():
        print("Before the function runs")   # extra code
        func()                              # original function call
        print("After the function runs")    # extra code
    return wrapper   # return wrapper instead of func

@my_decorator   # same as -> say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, World!")

say_hello()
# OUTPUT:
# Before the function runs
# Hello, World!
# After the function runs



# ------------------------------------
# 2. DECORATOR WITH ARGUMENTS (wrapper)
# ------------------------------------

def smart_divide(func):
    def wrapper(a, b):
        print(f"Dividing {a} by {b}")
        if b == 0:
            print("Oops! Cannot divide by zero")
            return
        return func(a, b)   # run original function
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))   # ✅ works
print(divide(5, 0))    # ❌ handled by decorator



# -------------------------------------------
# 3. DECORATOR WITH ANY NUMBER OF ARGUMENTS
# -------------------------------------------

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(4, 5))
# OUTPUT:
# Function add called with (4, 5) {}
# 9



# ---------------------
# 4. CLASS DECORATOR
# ---------------------

def add_str_method(cls):
    """
    This decorator modifies the class by adding __str__ method.
    """
    cls.__str__ = lambda self: f"This is object of class {cls.__name__}"
    return cls

@add_str_method
class MyClass:
    pass

obj = MyClass()
print(obj)   # OUTPUT: This is object of class MyClass



# ------------------------------------------------
# 5. CLASS AS DECORATOR (using __init__ + __call__)
# ------------------------------------------------

class DecoratorClass:
    def __init__(self, func):
        self.func = func   # store original function

    def __call__(self, *args, **kwargs):
        print("Before function")
        result = self.func(*args, **kwargs)
        print("After function")
        return result

@DecoratorClass
def greet(name):
    print(f"Hello {name}")

greet("Keshav")
# OUTPUT:
# Before function
# Hello Keshav
# After function



# ---------------------------------------------------
# REAL-WORLD USE CASES OF DECORATORS
# ---------------------------------------------------

# 1. Logging
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))

# 2. Authentication (dummy example)
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in", False):
            print("User not logged in!")
            return
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    print(f"Welcome {user['name']}! This is your profile.")

user1 = {"name": "Keshav", "logged_in": True}
user2 = {"name": "John", "logged_in": False}

view_profile(user1)   # allowed
view_profile(user2)   # blocked

# 3. Performance Measurement
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.5f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done with slow task!")

slow_function()

# =====================================================
# END OF NOTES
# =====================================================
