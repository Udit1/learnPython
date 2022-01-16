def checkPrime(number):
    is_prime = True
    for j in range(2, number):
        if number % j == 0:
            is_prime = False
    if is_prime == True:
        print(f"{number} is prime")
    else:
        print(f"{number} is non prime")


def check_prime_till(num):
    for i in range(1, num+1):
        checkPrime(i)


last_num = int(input("ENter the Last Number"))
check_prime_till(last_num)
