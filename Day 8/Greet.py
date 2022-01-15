def greet_with_name(name="User"):  # with Default Value
    print(f"Hello {name}!")


def greet(name):
    print("It is taking Input from Call Function", name)


greet_with_name("Udit")
greet_with_name()
greet(input("Enter your Name:"))
