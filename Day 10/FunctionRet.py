def fun(fname, lname):
    if fname == "" or lname == "":
        return "Invalid Strings"
    return (fname+" "+lname).title()


def Cap(fname, lname):
    return f"{fname.upper()} {lname.upper()}"


fname = input("Enter First Name")
lname = input("Enter Last Name")

print(fun(fname, lname))
print(Cap(fname, lname))
