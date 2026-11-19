"""Conexión a SQL Server para todos los casos.

Uso:
    from src.db import get_engine
    engine = get_engine()
    df = pd.read_sql("SELECT ...", engine)

Se configura con variables de entorno (opcional). Si no existen, usa los
valores por defecto: SQL Server local, autenticación de Windows.
"""
import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

SERVER = os.getenv("SQL_SERVER", r"localhost\SQLEXPRESS")
DATABASE = os.getenv("SQL_DATABASE", "ruta_datos")
DRIVER = os.getenv("SQL_DRIVER", "ODBC Driver 18 for SQL Server")


def connection_string(database: str = DATABASE) -> str:
    """Cadena ODBC con autenticación de Windows (sin usuario ni contraseña)."""
    return (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"  # necesario en local: el driver 18 cifra por defecto
    )


def get_engine(database: str = DATABASE) -> Engine:
    """Engine de SQLAlchemy, que es lo que usa pandas (read_sql / to_sql)."""
    params = quote_plus(connection_string(database))
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}", fast_executemany=True)
