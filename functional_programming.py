# -------------------------------
# 1. First-Class Functions
# -------------------------------
# Functions in Python can be stored in variables, passed as arguments, or returned.
def greet(name):
    return f"Hello {name}"

def call_func(func, value):
    return func(value)   # passing function as argument

print(call_func(greet, "Keshav"))  # Output: Hello Keshav


# -------------------------------
# 2. Higher-Order Functions
# -------------------------------
# Functions that take other functions as input OR return a function
def square(x):
    return x * x

def apply_func(func, numbers):
    return [func(n) for n in numbers]

print(apply_func(square, [1, 2, 3, 4]))  # Output: [1, 4, 9, 16]


# -------------------------------
# 3. map(), filter(), reduce()
# -------------------------------
nums = [1, 2, 3, 4, 5, 6]

# map → apply function to each element
squares = list(map(lambda x: x * x, nums))
print(squares)   # [1, 4, 9, 16, 25, 36]

# filter → keep only values that match condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4, 6]

# reduce → combine list into a single value
from functools import reduce
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)   # 21


# -------------------------------
# 4. Pure Functions
# -------------------------------
# Always same output for same input, no side effects
def pure_add(a, b):
    return a + b

print(pure_add(2, 3))   # 5


# -------------------------------
# 5. Lambda Functions
# -------------------------------
# Small anonymous functions (one-line functions)
double = lambda x: x * 2
print(double(5))   # 10


# -------------------------------
# 6. Closures
# -------------------------------
# Inner function remembers outer variable (even after outer ends)
def outer(x):
    def inner(y):
        return x + y   # x is remembered
    return inner

add5 = outer(5)   # outer stores x=5
print(add5(10))   # 15 (5+10)


# -------------------------------
# 7. Recursion
# -------------------------------
# Function that calls itself
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # 120
