import random

names = input("Enter everybody's names, separated by commas: ")
name_list = [name.strip() for name in names.split(',')]

paying_person = random.choice(name_list)

print(f"Today, {paying_person} will pay the bill!")
