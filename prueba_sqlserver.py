"""Prueba de conexión a SQL Server.

Correr desde la raíz de la plantilla:
    uv run python prueba_sqlserver.py

Si todo sale bien, imprime la versión de SQL Server y una tablita leída de la base.
"""
import pandas as pd
import pyodbc
from sqlalchemy import text

from src.db import DATABASE, DRIVER, connection_string, get_engine

# 1. ¿Está instalado el driver ODBC?
drivers = pyodbc.drivers()
print("Drivers ODBC instalados:", drivers)
if DRIVER not in drivers:
    raise SystemExit(f"Falta '{DRIVER}'. Instalalo desde la página de Microsoft y volvé a correr.")

# 2. ¿Responde el servidor? (se conecta a master, que siempre existe)
with pyodbc.connect(connection_string("master"), timeout=5) as cn:
    version = cn.execute("SELECT @@VERSION").fetchone()[0]
    print("\nConectado a SQL Server:\n", version.splitlines()[0])

    # 3. Crear la base de trabajo si no existe
    cn.autocommit = True
    cn.execute(f"IF DB_ID('{DATABASE}') IS NULL CREATE DATABASE [{DATABASE}]")
    print(f"\nBase '{DATABASE}' lista.")

# 4. Escribir y leer con pandas (lo que vas a usar en los casos)
engine = get_engine()
prueba = pd.DataFrame({"fuente": ["BCCR", "INEC", "CGR"], "fase": [1, 3, 2]})
prueba.to_sql("prueba_conexion", engine, if_exists="replace", index=False)

leido = pd.read_sql(text("SELECT fuente, fase FROM prueba_conexion ORDER BY fase"), engine)
print("\nLeído desde SQL Server:\n", leido)

# 5. Limpiar
with engine.begin() as conn:
    conn.execute(text("DROP TABLE prueba_conexion"))
print("\nTodo bien: Python lee y escribe en SQL Server.")
