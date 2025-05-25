import os
import pandas as pd

# Path to the CSV file
csv_path = 'example/C/.csv'

# Load the CSV file with semicolon as separator
df = pd.read_csv(csv_path, sep=';', on_bad_lines='skip')

# Extract the folder from the CSV file path
folder = os.path.dirname(csv_path)

# Create the path for the Parquet file in the same folder
parquet_path = os.path.join(folder, 'plik.parquet')

# Save to Parquet format
df.to_parquet(parquet_path, index=False)

print(f'Parquet file saved at: {parquet_path}')
