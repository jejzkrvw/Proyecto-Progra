import psycopg2 as psq

DB_NAME = "todo"
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"


try:
    conn = psq.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar a la base de datos:", e)
    conn = None
