print("""
-------------------------------------Pattern 1-------------------------------------""")
num = 5
for row in range(1, 5):
    for column in range(5, row+1, -1):
        print(num, end="")
    num -= 1
    print()
