total_bill_amt = float(input("Enter Total Bill amount ₹"))
tip_percentage = int(input("Enter Tip Percentage 10, 12 or 15 "))
num_of_people = int(
    input("Total Number of people among which the bill is to be divided ")
)

total_amt = total_bill_amt * (1 + (tip_percentage / 100))
share = total_amt / num_of_people
share = "{:.2f}".format(share)
print(
    f"Total Bill amount is ₹{total_bill_amt}, after adding tip of {tip_percentage}% the amount is ₹{total_amt}. Splitting in {num_of_people}, per head share is ₹{share}"
)
