height = float(input("How tall are you? (m)"))

mass = float(input("How heavy are you? (kg)"))

BMI = mass/(height*height)

print("Your BMI is ", BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Normal")
elif BMI <= 30:
    print("Overweight")
else:
    print("Obese")
