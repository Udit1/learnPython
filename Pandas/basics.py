import pandas as pd
import os

# df = pd.read_csv('Pandas/annual.csv')
# print(df.to_string())

# Normal Array to Table
# Length should be the same
mydataset = {
    'cars': ["BMW", "Volvo", "Ford", "Maruti"],
    'passings': [3, 7, 2, 6]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# check version of pandas
print(f"Pandas Version: {pd.__version__}")

# Series

name = ["A", "B", "C", "D"]
a = pd.Series(name)
print(a)


a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
