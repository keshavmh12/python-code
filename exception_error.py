# ===============================
# 🐍 Python Exception Handling
# ===============================

# 1. Basic try-except
try:
    x = 10 / 0   # risky code (division by zero)
except ZeroDivisionError:
    print("❌ Error: You cannot divide by zero!")

# --------------------------------

# 2. Multiple except blocks
try:
    num = int("abc")   # invalid conversion
except ValueError:
    print("❌ Error: Invalid conversion (string to int)")
except ZeroDivisionError:
    print("❌ Error: Division by zero not allowed")

# --------------------------------

# 3. Catching any exception
try:
    print(10 / 0)
except Exception as e:
    print("❌ General Error Caught:", e)

# --------------------------------

# 4. Using finally (always runs)
try:
    f = open("demo.txt")   # file may not exist
    print(f.read())
except FileNotFoundError:
    print("❌ Error: File not found")
finally:
    print("✅ Finally block: Always runs (cleanup code)")

# --------------------------------

# 5. Using else (runs only if no error)
try:
    result = 10 / 2   # no error here
except ZeroDivisionError:
    print("❌ Error: Division by zero")
else:
    print("✅ Else block: No error, result =", result)

# --------------------------------

# 6. Raising a custom exception
age = 15
try:
    if age < 18:
        raise ValueError("❌ Not eligible to vote (age must be 18+)")
except ValueError as e:
    print(e)

# --------------------------------

# 7. User-defined custom exception
class MyError(Exception):   # custom exception class
    pass

try:
    raise MyError("This is my custom error!")
except MyError as e:
    print("❌ Custom Exception Caught:", e)
