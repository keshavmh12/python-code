import json

filename = "contact_book.json"

#-----------load&save----------------

def load_contact():
   try:
       with open(filename,"r") as f:
             return json.load(f)
   except FileNotFoundError:
       return[]

def save_contact(contact):
    with open(filename,"w") as f:
        json.dump(contact,f,indent=4)

#-------------feature-----------------

def add_contact(contact):
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone number: ")

    contact.append({'name':name,'email':email,'phone':phone})
    save_contact(contact)
    print("Contact added successfully")

def view_contact(contact):
    print("\n--- Contact List ---")
    if not contact:  # check if empty
        print("No contacts found.")
    for c in contact:
        print(f"{c.get('name')}, {c.get('email')}, {c.get('phone')}")


def search_contact(contact):
    search=input("Enter your name: ")
    found=[c for c in contact if search.lower() in c.get('name','').lower()]

    if found:
        print("---search result---")
        for c in found:
            print(f"{c.get("name")},{c.get("email")},{c.get("phone")}")

    else:
        print("No contact found")


#-----------main menu-------------

def main():
    contact=load_contact()
    while True:
        print("\n---contact List---")
        print("1. Add a new contact")
        print("2. View contact")
        print("3. Search contact")
        print("4. Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            add_contact(contact)
        elif choice==2:
            view_contact(contact)
        elif choice==3:
            search_contact(contact)
        elif choice==4:
            print("Exiting contact book...")
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()

