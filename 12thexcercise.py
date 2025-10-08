size=input("which size fo pizza you want(s/m/l)?")
bill=0
if size=='s' or size=='S':
    bill+=100


elif size=='m' or size=='M':
    bill+=200

else:
    bill+=300


add_pepperoni=input("do you want pepperoni(Y/N)?")
if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='s'or size=='S':
        bill+=30
    else:
        bill+=50

add_cheese=input("do you want cheese(Y/N)?")
if add_cheese=='Y' or add_cheese=='y':
 bill+=20

print(f"your bill RS{bill}")