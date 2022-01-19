num = int(input("Enter any number"))


def checkNum(num):
    if num < 0:
        return "Negative"
    else:
        return "Positive"


print(checkNum(num))
