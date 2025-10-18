height=int(input("enter your height"))
if (height>3):
    print("you can drive ")
    age=int(input("enter your age"))
    if (age>=18):
        print("please pay 250")
    elif age<18:
        print("please pay 150")
    else:
        print("please pay 500")
else:
    print("you are not drive")
    print("byeee")