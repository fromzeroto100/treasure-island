height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

bmi = weight / height ** 2

print(int(bmi))

if bmi < 18.5:
    print("You are an underweight.")

elif bmi <= 25:
    print("You are a normal weight.")

elif bmi <= 30:
    print("You are a slightly overweight.")     

else:
    print("You are clinically obese. Stop eating such much.")

