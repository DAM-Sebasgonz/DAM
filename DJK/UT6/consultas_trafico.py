import sqlite3

DB_NAME = "trafico_red.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 1. Promedio de longitud de paquetes por protocolo
cursor.execute("""
    SELECT protocol, AVG(length) AS avg_length
    FROM packets
    GROUP BY protocol
    ORDER BY avg_length DESC
""")
print("Promedio de longitud por protocolo:")
for protocol, avg in cursor.fetchall():
    print(f"  {protocol} => {avg:.2f} bytes")

# 2. Intervalo temporal entre primer y último paquete
cursor.execute("""
    SELECT MIN(time) AS inicio, MAX(time) AS fin, MAX(time) - MIN(time) AS duracion
    FROM packets
""")
inicio, fin, duracion = cursor.fetchone()
print(f"\nCaptura iniciada en:  {inicio}")
print(f"Captura finalizada en: {fin}")
print(f"Duración total:        {duracion:.4f} segundos")

# 3. Top 5 IPs origen con más paquetes generados
cursor.execute("""
    SELECT source, COUNT(*) AS total
    FROM packets
    GROUP BY source
    ORDER BY total DESC
    LIMIT 5
""")
print("\nTop 5 IPs origen más activas:")
for i, (ip, total) in enumerate(cursor.fetchall(), start=1):
    print(f"  {i}. {ip} => {total} paquetes")

conn.close()