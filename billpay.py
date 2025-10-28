import random

name=input("enter name everyone separated by commas")
name_list=[name.strip() for name in name.split(',')]
paybill_person=random.choice(name_list)
print(f"todays paybill pay by the {paybill_person} ")
