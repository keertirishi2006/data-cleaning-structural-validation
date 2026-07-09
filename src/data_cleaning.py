import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw_dataset.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove extra spaces
df["Name"] = df["Name"].str.strip()

# Standardize email format
df["Email"] = df["Email"].fillna("Unknown")
df["Email"] = df["Email"].str.lower()

# Fill missing salary
df["Salary"] = df["Salary"].fillna(0)

# Standardize names
df["Name"] = df["Name"].str.title()

# Save cleaned data
df.to_csv("../data/cleaned_dataset.csv", index=False)

print("Cleaning Completed Successfully")