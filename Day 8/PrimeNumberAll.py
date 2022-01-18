
def check_prime_till(last_num):
    count_prime = 0
    prime_list = []
    for i in range(1, last_num+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime == True:
            count_prime += 1
            prime_list.append(i)
            print(f"{i} is prime")
        else:
            print(f"{i} is non prime")
    print(
        f"Total Prime Number Found from 1 till {last_num}: {count_prime}")
    print(f"{prime_list}")


last_num = int(input("Enter the Last Number"))
check_prime_till(last_num)
