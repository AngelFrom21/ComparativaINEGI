#lector de diccionario de datos INEGI:

import pandas as pd

#importación de datos del diccionario del INEGI
dic = pd.read_csv('fd_iter_cpv2010.csv' , encoding='latin-1')

#segmentación de datos: clave de indicador e indicador
ind = dic[['mnemonico','indicador']]

#impresión de los datos:
print(ind.head(50))