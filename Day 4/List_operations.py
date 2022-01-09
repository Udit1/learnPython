list1 = ["a", "b", "c"]
print(len(list1))

list1.append("d")  # or
list1[len(list1) :] = [123]  # append itterable only

print(list1)

list1.extend("HELLO")  # extends itterable only
list1[len(list1) :] = "Hello"
print(list1)


list1.insert(1, "OK")
print(list1)

a = list1.sorted()
print(a)
