# Calculate Body Mass Index
# BMI=weight(kg)/height**2
weight = int(input("Enter Your Weight in kg "))
height = float(input("Enter Your height in m "))

bmi = weight / (height * height)
print(f"{round(bmi)}")
