# Note:
# To Check condition always start with lower values

height = int(input("Enter Height in cm"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age"))
    if age < 12:
        bill = 25
        print("Child Ticket ₹25")
    elif age <= 18:
        bill = 50
        print("Youth Ticket ₹50")
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 100
        print("Adult Ticket ₹100")
    want_photo = input("Wants photos? Y or N")
    if want_photo == "Y":
        bill += 10
        print("added + ₹10 to bill")
    else:
        print("Enjoy the ride without photos")
    print(f"Please pay ₹{bill}")
else:
    print("Complane Piyo")
