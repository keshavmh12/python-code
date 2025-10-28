store_item={
    "rice":60,
    "wheat":45,
    "sugar":40,
    "milk":40,
    "oil":120,
    "salt":20,
}

cart={}

def display_menu():
    print("------------------Welcome to the APNA KIRANA------------------")
    for item,price in store_item.items():
        print(f"{item.title()}: {price}per unit")

def add_to_cart():
    item=input("Enter item to add: ")
    if item in store_item:
        qty=int(input("Enter quantity: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} units of {item} added to cart")
    else:
        print("Item not found")


def view_cart():
    if not cart:
        print("your cart is empty")
    else:
        print("your cart")

        total=0
        for item,qty in cart.items():
            price=store_item[item]
            cost=qty*price
            total += cost
            print(f"{item}: {qty} units of {item} added to cart")
            print(f"{item.title()}*{qyt}={cost}")
        print('Total bill:{total}')


def main():
    print("Welcome to the APNA KIRANA")

    while True:
        print("what would you like to do?")
        print("1. show grocery item")
        print("2. add item to cary")
        print("3. view cartv and total bill")
        print("4. exit")

        choice=int(input('Enter your choice(1-4)'))

        if choice==1:
            display_menu()
        elif choice==2:
            add_to_cart()
        elif choice==3:
            view_cart()
        elif choice==4:
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
main()