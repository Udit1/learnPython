def fibo(num):
    a = 0
    b = 1
    for i in range(0, num):
        print(a, end=" ")
        next = a+b
        a = b
        b = next


num = int(input("Enter Any number"))
fibo(num)
