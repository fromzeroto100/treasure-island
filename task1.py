print("Welcome to the rollercoaster! ")

height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        print("You should pay 7$")

    elif age <= 18:
          print("You should pay 10$")   
    else:
        print("You should pay 12$. ")
else:
    print("Sorry, you cannot ride.")   