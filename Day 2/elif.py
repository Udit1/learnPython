# Note:

# To Check condition always start with lower values

height = int(input("Enter Height in cm"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age"))
    if age < 12:
        print("Please Pay ₹25")
    elif age <= 18:
        print("Please Pay ₹50")
    else:
        print("Please Pay ₹100")
else:
    print("Complane Piyo")
