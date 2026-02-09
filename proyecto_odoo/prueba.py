import pandas as pd
import psycopg2

# Credenciales de PostgreSQL
db_config = {
    "host": "localhost",
    "database": "postgres",
    "user": "odoo",
    "password": "odoo",
    "port": 5432
}

archivo_csv = "listado.csv"

try:
    # Leer CSV con 'latin1' para manejar caracteres especiales
    df = pd.read_csv(archivo_csv, encoding="latin1")
    print("CSV leído correctamente")

    # Conectar con PostgreSQL
    conexion = psycopg2.connect(**db_config)
    cursor = conexion.cursor()

    # Eliminar la tabla si existe
    print("Eliminando tabla 'import_centros' si existe...")
    cursor.execute("DROP TABLE IF EXISTS import_centros;")
    conexion.commit()
    print("Tabla eliminada (si existía)")

    # Crear tabla con la estructura correcta
    cursor.execute("""
    CREATE TABLE import_centros (
        id SERIAL PRIMARY KEY,
        nombre TEXT,
        domicilio TEXT,
        telefono TEXT,
        municipio TEXT,
        provincia TEXT
    );
    """)
    conexion.commit()
    print("Tabla 'import_centros' creada correctamente")

    # Insertar datos usando iloc
    for i in range(len(df)):
        cursor.execute("""
        INSERT INTO import_centros (nombre, domicilio, telefono, municipio, provincia)
        VALUES (%s,%s,%s,%s,%s)
        """, (
            str(df.iloc[i, 2]),  # Nombre
            str(df.iloc[i, 4]),  # Domicilio
            str(df.iloc[i, 9]),  # Teléfono
            str(df.iloc[i, 6]),  # Municipio
            str(df.iloc[i, 7])   # Provincia
        ))

    conexion.commit()
    print("Datos insertados correctamente")

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
