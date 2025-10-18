# Generator function
def number_generator():
    for i in range(1, 6):
        yield i  # gives one number at a time

# Using the generator
for number in number_generator():
    print("Number:", number)
