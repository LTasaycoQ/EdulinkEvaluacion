import os
from flask import Flask, send_file, request, render_template, redirect, url_for, flash, session
from database.db import ActualizaContactos, eliminadContacto, nuevoContacto, obtener_contactos, obtener_contactos_inactivos, restaurarContactos, verificacionLogin, nueva_Cuenta

app = Flask(__name__, template_folder='src')
app.secret_key = os.urandom(24) 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard")
def layout():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('layout.html')

@app.route('/contactos')
def listar_contactos():
    if 'user' not in session:
        return redirect(url_for('index'))
    
    contactos = obtener_contactos()
    
    if contactos:
        return render_template('contactos.html', contactos=contactos)
    else:
        flash("No se encontraron contactos", "error")
        return render_template('contactos.html', contactos=[])



@app.route('/contactosInactivos')
def listar_contactos_inactivos():
    if 'user' not in session:
        return redirect(url_for('index'))
    
    contactos = obtener_contactos_inactivos()
    
    if contactos:
        return render_template('Papelera.html', contactos=contactos)
    else:
        flash("No se encontraron contactos", "error")
        return render_template('Papelera.html', contactos=[])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = verificacionLogin(email, password)
        if user:
            session['user'] = user[0]
            print("Exito")
            return redirect(url_for('listar_contactos'))
        else:
            print("Datos Iconrrector :(  Email o contraseña.")

    return render_template('index.html')
    
@app.route('/NuevaCuenta', methods=['POST'])
def NuevaCuenta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        user = nueva_Cuenta(nombre, email, password)

        if user:
            flash("Cuenta creada exitosamente! Ahora puedes iniciar sesión.", "success")
            return redirect(url_for('index'))
        else:
            flash("Error al crear la cuenta. Intenta nuevamente.", "error")
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/eliminar_contacto/<int:id>', methods=['POST'])
def eliminar_contacto(id):
    try:
        eliminado = eliminadContacto(id)

        
        print("Eliminado Exitoso")
        return redirect(url_for('listar_contactos'))
        
    except Exception as e:
        print(f"Error al eliminar el contacto: {e}")
        return "Error al eliminar el contacto", 500


@app.route('/restaurarContacto/<int:id>', methods=['POST'])
def restaurar_contacto(id):
    try:
        restaurar = restaurarContactos(id)

        
        print("Restauracion Exitoso")
        return redirect(url_for('listar_contactos_inactivos'))
        
    except Exception as e:
        print(f"Error al eliminar el contacto: {e}")
        return "Error al eliminar el contacto", 500


@app.route('/NuevoContacto', methods=['POST'])
def NuevoContacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        estado = "A"

        success = nuevoContacto(nombre, apellidos, direccion, telefono, email, estado)

        if success:
            flash("Contacto registrado con éxito", "success")
            return redirect(url_for('listar_contactos')) 
        else:
            flash("Error al registrar el contacto", "danger")
            return render_template('contactos.html')

    return render_template('contactos.html')




























@app.route('/editar_contacto/<int:id>', methods=['GET', 'POST'])
def editar_contacto(id):
    if request.method == 'POST':
        # Obtener los nuevos datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']

        try:
            ActualizaContactos(id, nombre, apellidos, direccion, telefono, email)

            return redirect(url_for('listar_contactos')) 
        except Exception as e:
            print(f"Error al editar el contacto: {e}")
            return "Error al editar el contacto", 500












@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

def main():
    app.run(port=int(os.environ.get('PORT', 80)))


if __name__ == "__main__":
    app.run(port=5001)

