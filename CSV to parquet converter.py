import os
import pandas as pd

# Ścieżka do pliku CSV
csv_path = 'example/C/.csv'

# Wczytanie pliku CSV z separatorem średnika
df = pd.read_csv(csv_path, sep=';', on_bad_lines='skip')

# Wydzielenie folderu z pliku CSV
folder = os.path.dirname(csv_path)

# Utworzenie ścieżki do pliku Parquet w tym samym folderze
parquet_path = os.path.join(folder, 'plik.parquet')

# Zapis do formatu Parquet
df.to_parquet(parquet_path, index=False)

print(f'Plik Parquet zapisany pod ścieżką: {parquet_path}')