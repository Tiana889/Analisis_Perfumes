
# Proyecto de Análisis de Perfumes

Este proyecto tiene como objetivo analizar y agrupar perfumes basados en descripciones de texto utilizando técnicas de procesamiento de lenguaje natural y clustering no supervisado. El análisis se enfoca en representar las descripciones de los perfumes como vectores numéricos y aplicar el algoritmo K-Means para agrupar perfumes similares.

## 1. Introducción
El conjunto de datos contiene información detallada de perfumes, como el nombre, marca, descripción, y las notas olfativas. Usamos un vectorizador TF-IDF para convertir las descripciones en representaciones numéricas, seguidas de K-Means para identificar grupos de perfumes similares.

## 2. Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes bibliotecas:
- pandas
- numpy
- sklearn
- matplotlib
- seaborn



## 3. Instrucciones de uso

1. Clona o descarga este repositorio.
2. Asegúrate de tener el archivo `final_perfume_data.csv` en la misma carpeta que el notebook.
3. Abre el notebook `PROYECTO FINAL.ipynb` y ejecuta las celdas de forma secuencial.

## 4. Análisis de los datos

- Se carga el conjunto de datos y se realiza una limpieza básica, identificando los tipos de datos y asegurando que las columnas importantes como `Name`, `Brand`, `Description`, y `Notes` están en el formato correcto.
  
- Se utiliza `pandas` para manipular el conjunto de datos y `seaborn` para visualizar correlaciones y patrones iniciales.

## 5. Modelado: Vectorización y Agrupamiento

### Vectorización TF-IDF:
Se utiliza el vectorizador TF-IDF para convertir las descripciones de texto de los perfumes en vectores numéricos. Esta técnica mide la importancia de palabras dentro de una colección de documentos, lo cual es crucial para capturar las características únicas de cada perfume.

### K-Means:
Después de vectorizar las descripciones, se aplica el algoritmo de K-Means para agrupar los perfumes en clusters. Cada cluster representa un conjunto de perfumes con descripciones y notas similares.

El número de clusters fue optimizado para asegurar que los grupos reflejen adecuadamente las similitudes entre perfumes.

## 6. Visualización de Resultados

Finalmente, los resultados del clustering se visualizan utilizando gráficos de reducción de dimensionalidad (PCA) y mapas de calor para explorar la distribución de los grupos.

## 7. Conclusiones

Este análisis proporciona una visión útil sobre cómo agrupar perfumes en función de sus descripciones. Los resultados permiten identificar qué perfumes tienen características similares y pueden ser agrupados dentro de un mismo segmento olfativo.
