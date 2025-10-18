# ---------------------------
# ITERATORS & GENERATORS
# ---------------------------

# 1️⃣ Normal Iterable (list) example
numbers = [1, 2, 3]
print("List itself is iterable but not an iterator.")
print("Type of numbers:", type(numbers))

# 2️⃣ Making an iterator using iter()
it = iter(numbers)  # convert list into iterator
print("\nIterator created from list.")
print(next(it))  # prints 1
print(next(it))  # prints 2
print(next(it))  # prints 3


# Uncomment below line to see error (StopIteration when elements finish)
# print(next(it))

# 3️⃣ Creating custom iterator using a class
class CountUpto:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self  # iterator object

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration  # stop iteration when limit reached


print("\nCustom Iterator Example:")
for x in CountUpto(5):
    print(x, end=" ")  # prints 1 2 3 4 5
print()


# ---------------------------
# GENERATORS
# ---------------------------

# 4️⃣ Generator function using yield
def simple_generator():
    yield "Hello"
    yield "from"
    yield "generator"


print("\nGenerator Example:")
gen = simple_generator()
print(next(gen))  # Hello
print(next(gen))  # from
print(next(gen))  # generator


# print(next(gen))  # StopIteration if uncommented

# 5️⃣ Generator for even numbers
def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i


print("\nEven numbers using generator:")
for val in even_numbers(10):
    print(val, end=" ")  # 0 2 4 6 8 10
print()

# 6️⃣ Generator Expression (like list comprehension but with round brackets)
squares = (x * x for x in range(5))
print("\nSquares using generator expression:")
for sq in squares:
    print(sq, end=" ")  # 0 1 4 9 16
print()

# ---------------------------
# DIFFERENCE SUMMARY
# ---------------------------
print("\n--- Difference ---")
print("Iterator: Uses __iter__() and __next__(), needs StopIteration.")
print("Generator: Uses 'yield', automatically handles iteration & StopIteration.")
