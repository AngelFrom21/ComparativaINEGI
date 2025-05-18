#extractor de datos: Natalidad y población adulta mayor (2010 vs 2020)

import pandas as pd

#datos de INEGI:
info2010 = pd.read_csv('iter_00_cpv2010.csv')
info2020 = pd.read_csv('conjunto_de_datos_iter_00CSV20.csv')

#corte previo a segmenación:

info2010 = info2010.drop([x for x in range(3)])
info2020 = info2020.drop([x for x in range(3)])

#segmentación de datos:

sec1 = info2010[['nom_ent','pnacent','pob65_mas']]
sec2 = info2020[['NOM_ENT','PNACENT','P_85YMAS']]

#limpieza:

#2010
sec1 = sec1.where((sec1['pnacent']!='*')&(sec1['pob65_mas']!='*'))
sec1 = sec1.where((sec1['pnacent']!='N/D')&(sec1['pob65_mas']!='N/D'))
sec1 = sec1.dropna()

#2020:

sec2 = sec2.where((sec2['PNACENT']!='*')&(sec2['P_85YMAS']!='*'))
sec2 = sec2.where((sec2['PNACENT']!='N/D')&(sec2['P_85YMAS']!='N/D'))
sec2 = sec2.dropna()

#conversion a flotantes:
#nacimientos y mayores 2010:
sec1['pnacent'] = sec1['pnacent'].apply(lambda x: float(x))
sec1['pob65_mas'] = sec1['pob65_mas'].apply(lambda x: float(x))

#nacimientos y mayores 2020:
sec2['PNACENT'] = sec2['PNACENT'].apply(lambda x: float(x))
sec2['P_85YMAS'] = sec2['P_85YMAS'].apply(lambda x: float(x))

#reumen de las variables:

sec1_r = sec1.groupby('nom_ent').sum()
sec2_r = sec2.groupby('NOM_ENT').sum()

#igualación de indices:

sec1_r.index = sec2_r.index

#impresión de los datos:
#print(sec1_r.head(10))
#print(sec2_r.head(10))

#construcción del dataframe final:

data = pd.DataFrame({
    'nom_ent': sec1_r.index,
    'nat 2010': sec1_r['pnacent'],
    'nat 2020': sec2_r['PNACENT'],
    'A.Mayor 2010': sec1_r['pob65_mas'],
    'A.Mayor 2020': sec2_r['P_85YMAS']
})

print(data.head())

data.to_csv('Comparativa_natvsmay.csv', index=False)