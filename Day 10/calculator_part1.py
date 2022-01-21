def addition(n1, n2):
    return n1+n2


def substract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


n1 = int(input("Enter Number 1: "))


operations = {"+": addition, "-": substract,
              "*": multiply, "/": divide}


for keys in operations:
    print(keys)

operation = input("Choose the Operation from Above:\t")
n2 = int(input("Enter Number 2: "))

calc = operations[operation]
print(calc)
ans = calc(n1, n2)
print(f"{n1} {operation} {n2} = {ans}")
