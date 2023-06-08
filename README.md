# Proyect_Plants

## Proyecto Plants to Plant

Este proyecto es un recomendador de plantas que utiliza parámetros proporcionados por el usuario para encontrar la planta que mejor se adapte a su estilo de vida. Se basa en datos de diferentes plantas, como su nombre, familia, género, orden, frecuencia de riego y si son plantas de interior o exterior. También ofrece información sobre la compatibilidad de las plantas según su pH para ser plantadas juntas.

### Características del proyecto

El proyecto está desarrollado utilizando Python, con el uso de la biblioteca Pandas para la limpieza y manipulación de datos.
La visualización interactiva se realiza utilizando Streamlit, una biblioteca de Python que permite crear aplicaciones web interactivas fácilmente.

Los datos utilizados para el recomendador de plantas son proporcionados y se almacenan en un archivo CSV.

El proceso ETL (Extracción, Transformación y Carga) se realiza mediante el uso de Pandas para limpiar y transformar los datos en un formato adecuado para el recomendador.

El recomendador de plantas utiliza los parámetros proporcionados por el usuario, como las preferencias de cuidado y el pH, para buscar y recomendar las plantas más adecuadas.

La recomendación se basa en un algoritmo que tiene en cuenta la frecuencia de riego, si la planta es de interior o exterior y la compatibilidad de pH con otras plantas.

### Estructura de archivos

main.py: Archivo principal que contiene el código para la ejecución del recomendador de plantas.

data.csv: Archivo CSV que contiene los datos de las plantas utilizados por el recomendador.

requirements.txt: Archivo que enumera las dependencias y bibliotecas necesarias para ejecutar el proyecto.

README.md: Este archivo, que proporciona una descripción general del proyecto y su funcionamiento.

## Cómo utilizar el recomendador de plantas

Al ejecutar el programa, se mostrará una interfaz de usuario donde se solicitarán los parámetros para la recomendación de plantas.

Proporciona la información solicitada, como tus preferencias de cuidado (frecuencia de riego, interior o exterior) y el pH de las plantas que deseas combinar.
El recomendador procesará la información y mostrará una lista de plantas recomendadas que se adaptan a tus preferencias y necesidades.
Puedes explorar la información detallada de cada planta recomendada, como su nombre, familia, género, orden y otros datos relevantes.