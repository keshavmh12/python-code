import random


name=input("enter everybody name, sepreted by comma: ")
seperate=name.split(',')
splited=seperate

paying_person=random.choice(splited)
print(f"today pay bill {paying_person}")