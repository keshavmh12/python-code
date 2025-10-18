# -------------------------------
# 1. Normal File Handling (without context manager)
# -------------------------------
# Problem: If an error occurs, file may not close properly
f = open("test.txt", "w")
f.write("Hello Keshav")
f.close()  # Must remember to close manually

# -------------------------------
# 2. Using Context Manager with "with"
# -------------------------------
# Benefit: File auto-closes after block, even if error happens
with open("test.txt", "w") as f:
    f.write("Hello Keshav")  # File closes automatically


# -------------------------------
# 3. Custom Context Manager (using __enter__ and __exit__)
# -------------------------------
class MyContext:
    def __enter__(self):
        print("Entered the context")
        return "Resource Ready"

    def __exit__(self, exc_type, exc_value, traceback):
        # Runs when block ends (even if error occurs)
        print("Exiting the context")


# Using custom context manager
with MyContext() as resource:
    print(resource)  # Output: Resource Ready

# -------------------------------
# 4. Custom Context Manager using contextlib
# -------------------------------
from contextlib import contextmanager


@contextmanager
def my_context():
    print("Entered the context")
    yield "Resource Ready"  # Value given to "as resource"
    print("Exiting the context")


with my_context() as resource:
    print(resource)  # Output: Resource Ready


# -------------------------------
# 5. Practical Example: Handling Errors
# -------------------------------
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_value}")
        return True  # Prevents program from crashing


# Using custom FileManager
with FileManager("data.txt", "w") as f:
    f.write("Data written successfully")
    # raise ValueError("Something went wrong")  # Uncomment to test error
