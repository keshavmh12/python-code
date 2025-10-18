def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add_numbers(1, 2, 3)         # Sum: 6
add_numbers(5, 10, 15, 20)   # Sum: 50



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Keshav", age=20, city="Pune")
# Output:
# name: Keshav
# age: 20
# city: Pune
