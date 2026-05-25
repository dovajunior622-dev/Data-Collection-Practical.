import pandas as pd

# Load CSV
data = pd.read_csv("students.csv")

print("--- CSV Head ---")
print(data.head())

print("\n--- CSV Info ---")
print(data.info())
