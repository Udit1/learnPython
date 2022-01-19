from audioop import ratecv


principal = float(input("Enter Principal Amount:\t"))
rate = float(input("Enter Rate:\t"))
time = int(input("Enter Time:\t"))

si = (principal*rate*time)/100
print(f"Calulated Simple Interst is = {si}")
