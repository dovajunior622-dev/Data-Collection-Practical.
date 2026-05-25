import pandas as pd

# Load the existing students CSV file
data = pd.read_csv("students.csv")

print("--- Checking for Missing Data ---")
print(data.isnull().sum()) # Check missing values

# Remove missing values
cleaned = data.dropna() 

# Save the cleaned data to a new CSV file
cleaned.to_csv("cleaned.csv", index=False)
print("\nData cleaning complete. 'cleaned.csv' has been created.")
