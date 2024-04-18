import pandas as pd 
import numpy as np

df_devoluciones = pd.read_excel('devoluciones.xlsx')

def limpiar_devoluciones(df):
    # Se rellena los nulos con 'NA' para los campos categóricos
    # y con cero para los campos numéricos.
    df.fillna({'CVE_VEND': 'NA', 'CVE_PEDI': 'NA', 'DOC_ANT': 'NA'}, inplace=True)
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    return df

devoluciones_limpio = limpiar_devoluciones(df_devoluciones)

# Guardar los datos limpios en un nuevo archivo CSV
devoluciones_limpio.to_csv('devoluciones_limpio.csv', index=False)

