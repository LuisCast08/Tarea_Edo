

from dash import Dash, html, dcc
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objects as go
import warnings
import math
import re

def fxn():
    warnings.warn("deprecated", DeprecationWarning)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize":(8,4)} )


dfc = pd.read_csv("C:/Users/luisc/OneDrive/Documentos/xd/accidents_clean.csv")
dfe = pd.read_csv("C:/Users/luisc/OneDrive/Documentos/xd/comisiones.csv" )
dfs = pd.read_csv("C:/Users/luisc/OneDrive/Documentos/xd/emisiones.csv") 
dfa = pd.read_csv("C:/Users/luisc/OneDrive/Documentos/xd/siniestros.csv")

dfa = dfa.dropna(axis =0, subset="EDAD")

dfa['EDAD'] = dfa['EDAD'].astype(int)
print(dfa["EDAD"].head())

def limpf (n):
  if type(n) == str: #Identifica si el tipo de dato de n es str
    if ',' in n: #Identifica si el str tiene una coma
      n = n.replace(',','') # Se elimina las comas del int si tiene coma
      try: 
        n = float(n) #Se convierte a float el valor si al intentar convertir n a float arroja un valor True 
      except ValueError:
        n=n # Si el valor arroja False al intentar convertir a float el valor lo deja igual
    try:
      float(n)
      return float(n) #Se convierte a float el valor si al intentar convertir n a float arroja un valor True 
    except ValueError: # Si el valor no se puede converir a float:
      if n == 'No disponible ':
        n = 0 # Si el dato es igual a "No disponible " lo convierte a 0
      else: 
        return n # Si no cumlpe algun criterio anterior se mantiene el mismo valor
      return n
  else:
    return float(n) #Si el tipo de dato de n no es str se convierte a float
  
def limdfn(d,fun): #Limpiar un DataFrame convirtiendo los numeros str en valores float
  ndf = pd.DataFrame()
  for c in d.columns:
    ndf[c] = d[c].apply(fun)
  return ndf

dfso = limdfn(dfs,limpf)


dfco = limdfn(dfc,limpf)




def grouped_bar_chart(df, colum_nam, columna_valores='SEXO', top_n=6):
    # Agrupar el DataFrame por labels y calcular la cantidad de apariciones de cada valor
    dataframe_agrupado = df.groupby([colum_nam, columna_valores]).size().unstack()

    # Calcular la suma total de apariciones de cada label y ordenar de mayor a menor
    suma_total = dataframe_agrupado.sum(axis=1).sort_values(ascending=False)

    # Seleccionar los 'top_n' mejores resultados
    mejores_labels = suma_total.head(top_n).index
    dataframe_mejores = dataframe_agrupado.loc[mejores_labels]

    # Crear el gráfico de barras agrupadas con Plotly
    fig = sp.make_subplots(specs=[[{"secondary_y": True}]])
    for i, columna in enumerate(dataframe_mejores.columns):
        fig.add_trace(go.Bar(x=dataframe_mejores.index, y=dataframe_mejores[columna], name=columna), secondary_y=False)

    # Personalizar gráfico
    fig.update_layout(title_text=f'Gráfico de barras agrupadas para {colum_nam} los (Top {top_n} resultados) por género',
                      xaxis_title=colum_nam, yaxis_title='Cantidad de apariciones')

    # Mostrar gráfico
    fig.show()

luis = grouped_bar_chart(dfco,'ENTIDAD')
andres =grouped_bar_chart(dfso,'ENTIDAD')
santiago = grouped_bar_chart(dfso,'ENTIDAD')

