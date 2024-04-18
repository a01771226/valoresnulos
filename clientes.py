import pandas as pd
clientes_df = pd.read_excel('clientes.xlsx')

def limpiar_clientes(df):
    df['RFC'].fillna('NA', inplace=True)
    df['NOMBRE'].fillna('ANONIMO', inplace=True)
    return df

# Aplicamos la función de limpieza
clientes_limpio = limpiar_clientes(clientes_df)

# Guardamos el DataFrame limpio en un nuevo archivo CSV
clientes_limpio.to_csv('clientes_limpio.csv', index=False)