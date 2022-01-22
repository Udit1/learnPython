global_var = 20
other_var = 40


def fun():
    local_var = 10
    global_var = 30
    print(f"{local_var, global_var} before changes")
    # if we want to add 10 in global var by changing other_var+=10
    # other_var+=10   #it won't work
    # to use global var
    global other_var
    print(f"Before the change {other_var}")
    other_var += 10
    print(f"After the change {other_var}")


fun()
print(other_var)  # It will permanent change to global var
