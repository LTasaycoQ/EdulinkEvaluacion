import os
import psycopg2
from flask import Flask, send_file, request, render_template, redirect, url_for, flash, session

app = Flask(__name__, template_folder='src')

app.secret_key = os.urandom(24)  # Necesario para usar sesiones y flash

# URL de conexión a la base de datos (necesitarás reemplazarla si cambia)
DB_URL = "postgresql://neondb_owner:npg_ZdmSnuWj9e4x@ep-cold-dust-a88j4gh3-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&options=endpoint%3Dep-purple-snow-a5b2y909"

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/Perfil")
def perfil():
    # Verificar si el usuario está autenticado
    if 'user' not in session:
        return redirect(url_for('index'))  # Redirige al login si no está autenticado
    return send_file('src/perfil.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            connection = psycopg2.connect(DB_URL)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM person WHERE email = %s AND password = %s", (email, password))
            user = cursor.fetchone()

            if user:
                session['user'] = user[0]  
                return redirect(url_for('perfil'))  # Redirige al perfil si es exitoso
            else:
                flash("Email o contraseña incorrectos.")  # Mensaje de error si no se encuentra el usuario

            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Error al conectar con la base de datos :(  : {e}")
            flash("Hubo un error al procesar tu solicitud.")

    return render_template('index.html')  # Muestra el formulario de login

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
