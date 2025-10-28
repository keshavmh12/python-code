from tkinter import image_names

paans = ['small_paan', 'medium_paan', 'big_paan', 'family_pack_paan']
print("WELCOME TO THE MAHAYUG PAANSHOP")
print("which type of paan you want")
for paan in paans:
    print(f"{paan}")

price={
'small_paan':120,
'medium_paan':160,
'big_paan':200,
'family_pack_paan':220
}

name = input("What is your name?")
selected_paan=input("which paan you want?")
if selected_paan in price:
    price=price[selected_paan]
    print(f'{selected_paan.replace('_',' ').title()} rate: rs{price}')

    order=input("order confirm or not confirm?").strip().lower()
    if order == "order confirm":
        print(f'{selected_paan} paan order confirmed. \n plz pay rs{price}')
    else:
        print('order cancelled')

else:
    print(f"{selected_paan} paan not found.")



