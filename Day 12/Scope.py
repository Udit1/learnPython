""" Two Types of Variable
1. Local
2. Global

"""
global_var = 10


def fun():
    print(global_var)
    local_var = 20
    print(local_var)


if global_var == 10:
    """ Accessible outside"""
    scope_var = 30

# print(local_var) #Can't Accessible
print(global_var)
fun()
print(scope_var)
