import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('data/all_players.csv')

print(f"Original data shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Standardize column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Remove rows with missing essential information (using actual column names)
initial_rows = len(df)
df = df.dropna(subset=['fullname', 'country_name'])
print(f"Removed {initial_rows - len(df)} rows with missing name or country")

# Example: Fill missing numeric fields with appropriate values
num_cols = df.select_dtypes('number').columns
df[num_cols] = df[num_cols].fillna(0)

# Remove duplicate players (based on fullname and country)
initial_rows = len(df)
df = df.drop_duplicates(subset=['fullname', 'country_name'])
print(f"Removed {initial_rows - len(df)} duplicate players")

print(f"Final cleaned data shape: {df.shape}")

# Save cleaned data for further use
df.to_csv('data/cleaned_all_players.csv', index=False)
print("Cleaned data saved to 'data/cleaned_all_players.csv'")
