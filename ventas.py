import pandas as pd

df=pd.read_csv("Ventas_totales.csv")
print(df)

df['salon_ventas'] = df['salon_ventas'].fillna(round(df['salon_ventas'].mean(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['tarjetas_debito'] = df['tarjetas_debito'].fillna(round(df['tarjetas_debito'].median(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['tarjetas_credito'] = df['tarjetas_credito'].fillna(round(df['tarjetas_credito'].median(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['otros_medios'].describe()

df['otros_medios']

df['otros_medios']=df['otros_medios'].fillna(6922148.759)
valores_nulos=df.isnull().sum()
valores_nulos

df['subtotal_ventas_alimentos_bebidas'] =df['subtotal_ventas_alimentos_bebidas'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
valores_nulos

df['bebidas'] =df['bebidas'].fillna(round(df['bebidas'].median(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['almacen'] =df['almacen'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
valores_nulos

df['panaderia'] =df['panaderia'].fillna(0)
valores_nulos=df.isnull().sum()
valores_nulos

df['lacteos'] =df['lacteos'].fillna(0)
valores_nulos=df.isnull().sum()
valores_nulos

df['carnes'] =df['carnes'].fillna(round(df['carnes'].median(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['verduleria_fruteria'] =df['verduleria_fruteria'].fillna(method='bfill')
valores_nulos=df.isnull().sum()
valores_nulos

df['alimentos_preparados_rotiseria'] =df['alimentos_preparados_rotiseria'].fillna(method='ffill')
valores_nulos=df.isnull().sum()
valores_nulos

df['indumentaria_calzado_textiles_hogar'] =df['indumentaria_calzado_textiles_hogar'].fillna(round(df['indumentaria_calzado_textiles_hogar'].mean(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['electronicos_articulos_hogar'] =df['electronicos_articulos_hogar'].fillna(round(df['electronicos_articulos_hogar'].median(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df['otros'] =df['otros'].fillna(round(df['otros'].mean(),1))
valores_nulos=df.isnull().sum()
valores_nulos

df.to_csv('Ventas_totales_limpio.csv')