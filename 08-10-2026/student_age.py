import pandas as pd
import re

df = pd.read_csv(r"C:\Users\Sakshi\Documents\APC Lab(sem-5)\08-10-2026\age.csv")

current_year = 2026

df["Age"] = df["Birthdate"].apply(
    lambda x: current_year - int(re.findall(r"\d{4}", x)[0]))

print(df[["Roll No", "Name", "Birthdate", "Age"]])