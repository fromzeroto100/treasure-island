print("Welcome to the rollercoaster! ")
bill = 0
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 7
        print("Price for children 7$")

    elif age <= 18:
        bill = 10 
        print("Price for youth 10$")   
    elif age >= 45 and age <= 55:
        print("It is free for you!")

    else:
        bill = 12
        print("Price for adults 12$. ")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or "y":
        bill += 3
    print(f"Your bill is {bill}")
else:
    print("Sorry, you cannot ride.")   
