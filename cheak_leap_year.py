sum=0
while(True):
    user_input=int(input("enter the product price & press Q for quit"))
    if user_input != 'q':
        sum=sum+user_input
        print(f"order total so far:{sum}")
    else:
        print(f"your total bill is{sum}. thanks for shopping withs us")
        break