import pandas as pd
import numpy as np

# Cargar el archivo
df_notas = pd.read_excel('notas_credito.xlsx')

# Eliminar la columna 'Unnamed: 0' si está presente
if 'Unnamed: 0' in df_notas.columns:
    df_notas.drop(columns=['Unnamed: 0'], inplace=True)

# Llenar valores faltantes en 'CVE_VEND' con 0
df_notas['CVE_VEND'].fillna(0, inplace=True)

# Eliminar filas donde 'CVE_PEDI' sea NaN
df_notas.dropna(subset=['CVE_PEDI'], inplace=True)

# Eliminar duplicados basados en 'CVE_DOC'
df_notas.drop_duplicates(subset=['CVE_DOC'], inplace=True)

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_notas.to_csv('notas_credito_limpio.csv', index=False)
