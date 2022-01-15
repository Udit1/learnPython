def checkPrime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else:
        print("Non Prime")


for a in range(10):
    number = int(input("Enter Number"))
    checkPrime(number)
