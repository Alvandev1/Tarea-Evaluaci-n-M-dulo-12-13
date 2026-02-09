# Proyecto de Automatización de Datos en Odoo con Python

## Descripción

Este proyecto consiste en la **automatización de la carga de datos** desde un archivo CSV a una base de datos PostgreSQL utilizada por **Odoo**. Se ha desarrollado un script en Python para realizar un proceso **ETL** (Extracción, Transformación y Carga) que lee el archivo CSV, crea la tabla necesaria en la base de datos y carga los datos en ella.

## Estructura del Proyecto

- **prueba.py**: Script en Python para realizar la conexión con la base de datos, crear la tabla e insertar los datos del archivo CSV.
- **listado.csv**: Archivo CSV que contiene los datos de centros educativos.
- **README.md**: Documento explicativo de cómo configurar y ejecutar el proyecto.

## Requisitos

Para ejecutar el proyecto, necesitas tener instalados los siguientes elementos:

- **Python 3.10+**
- **Bibliotecas Python**:
  - pandas
  - psycopg2-binary

Puedes instalar las bibliotecas necesarias ejecutando:

```bash
pip install pandas psycopg2-binary
