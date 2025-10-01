weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height ** 2)

if BMI < 18:
    print("You are underweight")
elif BMI >= 18 and BMI <= 25:
    print("You are in normal weight")
elif BMI > 25 and BMI <= 30:
    print("You are overweight")
else:
    print("You are obese")
