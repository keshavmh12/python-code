height=int(input("enter your height"))
bill=0
if(height>3):
  print("you can ride")
  age=int(input("enter your age"))
  if(age<12):
      bill=150
      print("pay 150 rs")
  elif(age>=12 and age<=18):
      bill=200
      print("pay 200 rs")
  else:
      bill=500
      print("pay 500 rs")

      want_photo=input("you want photo (Y/N)?")
      if want_photo=='Y' or want_photo=='y':
         bill = bill + 50
      print(f"pay your bill {bill}")




else:
 print("you can not ride")