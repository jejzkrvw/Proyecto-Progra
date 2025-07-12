from ToDo_list.db.db import conn

cursor =conn.cursor()



def alta_actividad(data):
        if not data["titulo"] or not data ["actividad"] or not data["fecha"]:
            return(False, "Actividad, descripcion y fecha son obligatorios")
        try:
            cursor.execute("""INSERT INTO actividades (titulo, actividad, fecha) VALUES (%s, %s, %s)""", (data["titulo"], data["actividad"], data["fecha"]))
            conn.commit()
            return (True, "La actividad se registro con exito")
        except Exception as e:
            print(e)
            return (False, "Ocurrio un error al guardar la actividad")
        
def get_all_activities():
    cursor.execute("SELECT * FROM actividades ORDER BY  id")
    usuarios = cursor.fetchall()
    print(usuarios)
    return usuarios

def delete_activities(user_id):
    cursor.execute("DELETE FROM actividades WHERE id = %s", (str(user_id,)))
    conn.commit()