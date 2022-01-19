print("""
-------------------------------------Pattern 1-------------------------------------""")
num = 10
for row in range(1, 5):
    for column in range(1, row+1):
        print(num, end=" ")
        num -= 1
    print()
