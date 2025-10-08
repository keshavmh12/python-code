import random
from stringprep import in_table_c4

latter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','&','*','(',')','_','=']
number=[0,1,2,3,4,5,6,7,8,9]
print("welcome to the password generator")
n_letter=int(input("how much letter you want in your password?"))
n_symbol=int(input("how much symbol you want in your password?"))
n_number=int(input("how many numbers you want in your password?"))
password=[]
for i in range(1,n_letter+1):
    char=random.choice(latter)
    password+=char
for i in range(1,n_symbol+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,n_number+1):
    char=random.choice(number)
    password+=char
print(password)
random.shuffle(password)
print(password)
passwordd=""
for char in password:
    passwordd+=char
print(passwordd)
