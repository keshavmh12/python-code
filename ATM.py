correc_pin="1234"
balance=10000
pin=input("enter the pin :")
if pin==correc_pin:
    print(f"VERIFIED PIN1234")

    while True:
        print("1.check balance")
        print("2.withdraw")
        print("3.deposite")
        print("4.exit")

        choice=int(input('enter your choice (1-4):'))

        if choice==1:
            print(f"your balance is {balance}")

        elif choice==2:
         withdraw=int(input("how much do you want withdraw:"))
         balance-=withdraw
         print(f"your remaining balance is {balance}")

        elif choice==3:
             print(f"your current balance is {balance}")
             deposite=int(input("how much do you want deposite:"))
             balance+=deposite
             print(f"your current balance is {balance}")

        elif choice==4:
                 print("THANK YOU ! \n have a nice day")
                 break

else:
    print("UNVERIFIED PIN")