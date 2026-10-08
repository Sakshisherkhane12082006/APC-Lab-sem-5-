import pandas as pd

data = pd.read_csv(r"C:\Users\Sakshi\Documents\APC Lab(sem-5)\08-10-2026\names.csv")

series = data["Name"]

print("Name Series:")
print(series)