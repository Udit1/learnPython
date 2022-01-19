# 5! = 5x4x3x2x1

number = int(input("Enter a Number to get Factorial\t"))
factorial = 1
list1 = []
for i in range(1, number+1):
    factorial = factorial*i
    list1.append(str(i))

print(factorial)
print(f"{number}! = {' x '.join((reversed(list1)))} = {factorial}")
