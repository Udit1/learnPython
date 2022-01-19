print("""
-------------------------------------Number Pattern-------------------------------------""")

for row in range(1, 5):
    for column in range(1, row+1):
        print(row, end="")
    print()

print("""
-------------------------------------Number Pattern 2-------------------------------------""")

for row in range(1, 5):
    for column in range(1, row+1):
        print(column, end="")
    print()


print("""
-------------------------------------Number Pattern 3-------------------------------------""")

for row in range(1, 5):
    for column in range(5, row, -1):
        print(row, end="")
    print()

print("""
-------------------------------------Star Pattern-------------------------------------""")
for row in range(0, 5):
    for column in range(0, row):
        print("*", end="")
    print()


print("""
-------------------------------------Star Pattern 2-------------------------------------""")

for row in range(1, 5):
    for column in range(5, row, -1):
        print(" ", end="")
    for stars in range(1, row):
        print(" *", end="")
    print()


print("""
-------------------------------------Star Pattern 3-------------------------------------""")
number = 1
for row in range(1, 5):
    for column in range(1, row+1):
        print(number, end=" ")
        number += 1
    print()
