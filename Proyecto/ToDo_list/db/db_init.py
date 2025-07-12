from ToDo_list.db.db import conn

sql_schema = """
    CREATE TABLE IF NOT EXISTS actividades (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    actividad VARCHAR(100) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"""

def iniciar_db():
    try:
       
       cursor = conn.cursor()
       cursor.execute(sql_schema)
       conn.commit()
       print("Tablas creadas con exito")
    except Exception as e:
        print(e)   

iniciar_db()