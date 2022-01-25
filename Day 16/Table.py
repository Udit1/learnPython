from prettytable import PrettyTable
x = PrettyTable()

print(x)

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)

print("_________________________________________________")
o_table = PrettyTable()

o_table.add_column("Name", ["Ram", "Krishna", "Vivekanand"])
o_table.add_column("Place Of Birth", ["Ayodhya", "Mathura", "Kolkata"])
o_table.add_column("Yug", ["Satyug", "Dwaparyug", "Kalyug"])

print(o_table)

another = PrettyTable()
another.add_rows("Hello")

one_another = PrettyTable()
one_another.field_names = ["Name"]
one_another.add_row(["Ok               "])

print(another)
one_another.align = "c"

print(one_another)
