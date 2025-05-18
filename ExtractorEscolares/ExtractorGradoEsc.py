#Extractor: Grado promedio de escolaridad por entidad federativa

import pandas as pd

#fuente de datos:
#escolaridad 2010:
info1 = pd.read_csv('iter_00_cpv2010.csv')
#escolaridad 2020:
info2 = pd.read_csv('conjunto_de_datos_iter_00CSV20.csv')


#limepieza de encabezados:

info1 = info1.drop([x for x in range(3)])
info2 = info2.drop([x for x in range(3)])

#seccionado de datos:

sec1 = info1[['nom_ent','graproes']]
sec2 = info2[['NOM_ENT','GRAPROES']]

#limpieza de nulos:

#2010
sec1 = sec1.where((sec1['graproes']!='*'))
sec1 = sec1.where((sec1['graproes']!='N/D'))
sec1 = sec1.dropna()

#2020
sec2 = sec2.where((sec2['GRAPROES']!='*'))
sec2 = sec2.where((sec2['GRAPROES']!='N/D'))
sec2.dropna()

#conversion a operables (flotantes).

sec1['graproes'] = sec1['graproes'].apply(lambda x: float(x))
sec2['GRAPROES'] = sec2['GRAPROES'].apply(lambda x: float(x))

#resumen de datos:

sec1_r = sec1.groupby('nom_ent').mean()
sec2_r = sec2.groupby('NOM_ENT').mean()

#igualación de indices:

sec1_r.index = sec2_r.index

#primera imp:

#print(sec1_r.head())
#print(sec2_r.head())

#datos finales

data= pd.DataFrame({
    'nom_ent': sec1_r.index,
    'gradprom 2010': sec1_r['graproes'],
    'gradprom 2020': sec2_r['GRAPROES']
})

print(data.head())

data.to_csv('Comparativa_grados2010vs2020.csv', index=False)