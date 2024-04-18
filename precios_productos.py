import pandas as pd
import numpy as np

df_precios = pd.read_excel('precios_productos.xlsx')

df_precios.drop(columns=['Unnamed: 0'], inplace=True)

# Llenar valores faltantes en 'NOMBRE_CLIENTE' y 'DESCR'
df_precios['NOMBRE_CLIENTE'].fillna('DESCONOCIDO', inplace=True)
df_precios['DESCR'].fillna('SIN DESCRIPCION', inplace=True)

# Eliminar duplicados basados en 'CVE_DOC'
df_precios.drop_duplicates(subset=['CVE_DOC'], inplace=True)

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_precios.to_csv('precios_productos_limpio.csv', index=False)
