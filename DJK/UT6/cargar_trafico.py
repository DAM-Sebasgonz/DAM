import sqlite3
import csv

DB_NAME = "trafico_red.db"
CSV_FILE = "./trafico_red.csv"

# Conexión a la base de datos (si no existe, se crea)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS packets (
        no INTEGER,
        time TEXT,
        source TEXT,
        destination TEXT,
        protocol TEXT,
        length INTEGER,
        info TEXT
    )
""")

# Limpiar la tabla por si ya tenía datos
cursor.execute("DELETE FROM packets")

# Abrir el CSV y cargarlo
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # leer cabecera
    for row in reader:
        cursor.execute("""
            INSERT INTO packets (no, time, source, destination, protocol, length, info)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            row[0],                          # No.
            row[1],                          # Time
            row[2],                          # Source
            row[3],                          # Destination
            row[4],                          # Protocol
            row[5],                          # Length
            row[6] if len(row) > 6 else ""   # Info
        ))

conn.commit()
conn.close()

print("Datos cargados correctamente.")