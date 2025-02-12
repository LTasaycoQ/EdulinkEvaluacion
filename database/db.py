import psycopg2
from config import DB_URL

def verificacionLogin(email, password):
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM person WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user
    except Exception as e:
        print("Error al conectar con la base de datos: {e}")
        return None



def nueva_Cuenta(nombre, email, password):
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO person (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
        connection.commit()

        cursor.execute("SELECT * FROM person WHERE email = %s", (email,))
        new_user = cursor.fetchone()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        new_user = None
    finally:
        cursor.close()
        connection.close()

    return new_user




def obtener_contactos():
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("SELECT id, nombre, apellidos, direccion, numerotelefono, email FROM Contactos Where estado='A'")
        contactos = cursor.fetchall()

        cursor.close()
        connection.close()

        return contactos
    except Exception as e:
        print(f"Error al obtener los contactos: {e}")
        return None





def obtener_contactos_inactivos():
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("SELECT id, nombre, apellidos, direccion, numerotelefono, email FROM Contactos Where estado='I'")
        contactos = cursor.fetchall()

        cursor.close()
        connection.close()

        return contactos
    except Exception as e:
        print(f"Error al obtener los contactos: {e}")
        return None



import psycopg2

def nuevoContacto(nombre, apellidos, direccion, telefono, email, estado):
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO contactos (nombre, apellidos, direccion, numerotelefono, email, estado) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (nombre, apellidos, direccion, telefono, email, estado))

        connection.commit()

        print("Contacto registrado con éxito.")
        return True  
    
    except Exception as e:
        print(f"Error al conectar con la base de datos o insertar los datos: {e}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()





def eliminadContacto(id):
    try:
       
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("UPDATE Contactos SET estado = 'I' WHERE Id = %s", (id,))
        connection.commit();
    
        print("Contacto Eliminado Logicamente.")
        return True  
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False
    finally:
        cursor.close()
        connection.close()
        return False





def restaurarContactos(id):
    try:
       
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("UPDATE Contactos SET estado = 'A' WHERE Id = %s", (id,))
        connection.commit();
    
        print("Contacto Restaurado")
        return True  
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return False
    finally:
        cursor.close()
        connection.close()
        return False






def ActualizaContactos(id, nombre, apellidos, direccion, telefono, email):
    try:
        connection = psycopg2.connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Contactos
            SET nombre = %s, apellidos = %s, direccion = %s, numerotelefono = %s, email = %s
            WHERE id = %s
        """, (nombre, apellidos, direccion, telefono, email, id))

        connection.commit()
        cursor.close()
        connection.close()
    
        print("Contacto Actualizado Correctamente.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

