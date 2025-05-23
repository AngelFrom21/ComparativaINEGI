# Comparativa: Natalidad, población adulta mayor y grado escolar promedio (2010 vs 2020)
Este repositorio contiene los archivos para realizar comparativas poblacionales y sus datos relevantes usando los datos de accesos abierto del INEGI (2010 y 2020), los archivos que contienen los datos se encuentran en la siguiente carpeta de google drive debido a que GitHub no permite subidas mayores a 25MB, enlace: https://drive.google.com/drive/folders/1XXtfpqG4Kwza4wv_zKcWwVqiir0vcJZQ?usp=sharing

## Sobre este proyecto: Natalidad y población adulta mayor (2010 vs 2020)
El objetivo de este proyecto es comparar el cambio en la natalidad y población de adultos mayores en el tiempo (**10 años**) para estimar que población crece más rápido y poder determinar (**por entidad federativa**) cambios presupuestales en base a la prioridad poblaciónal.

## Sobre este proyecto: Grado escolar promedio por entidad federativa (2010 vs 2020)
El repositorio  contiene el archivo para extraer los datos sobre el grado escolar promedio de cada entidad federativa como promedio de sus municipios, la finalidad del mismo es evidenciar el promedio de cada entidad en el paso del tiempo para determinar que entidades deben ser apoyadas en este aspecto así cómo establecer posibles causas de estos promedios.

## Aspectos a tener en cuenta sobre los datos empleados
Los siguientes aspectos deben ser considerados para los datos INEGI2020:
1. Los datos de algunas entidades podrian no estar completos a causa de que en este año surgio la contingencia de COVID19
2. El estado de **Colima** presenta una falta considerable de información, posiblemente a causa de la contingencia del virus, esto ocaciona un sesgo importante a falta de datos.
3. Unicamente se emplean datos de 10 años de diferencia pues la página oficial del INEGi solo tiene registro del 2010 y 2020.

## Sobre la visualización de datos
Respecto a la visualización de los datos procesados, se eligío emplear PowerBi como herramienta de visualización a causa de que sus gráficos son, para este caso, los más adecuados, los resultados de estos análisis pueden consultarse en la liga: https://drive.google.com/drive/folders/1XXtfpqG4Kwza4wv_zKcWwVqiir0vcJZQ?usp=sharing


## Instrucciones de uso
Para ejecutar correctamente el lector y los extractores:
1. descargar tanto los archivos de este repositorio (ExtractoresLector) como los archivos CSV proporcionados en la carpeta de google drive proporcionada en secciones anteriores.
2. los archivos, una vez descargados **deberán** estar todos en una misma carpeta (**asegurese de que es así, de otra forma los extractores no podrán localizar los datos**).
3. En caso de querer utilizar la versión NB de estos archivos, unicamente considerar el paso 2.
4. ejecutar el archivo, ya sea con un compilador (Spyder, VS code etc) o usando Jupyter/ Colab.

**Importante:** estos archivos proporcionan unicamente datos procesados, la visualización se deja a criterio del usuario ( se recomienda usar PowerBi debido a que los indices de las entidades se muestran pequeños al utilizar librerias típicas de python) 
