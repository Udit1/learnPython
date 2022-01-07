# These are the basic DataTypes
string1 = "Hello World"
integer1 = 10105555
float1 = 101.10

print(string1, integer1, float1)

# To print any number in string I need to convert the data type to string

print("These are the values" + string1 + str(integer1) + str(float1))
# To format this better using f-string
print(f"These are the values {string1} {integer1} {float1}")

# To make an integer more readable use _
print(101_555_55)

# round
print(round(float1, 2))
# as it will print 101.1, but it should be like 101.10
# then we will use format for float
print("This should be like {:.2f}".format(float1))

print("Hello World {:.1}".format("Udit"))
