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