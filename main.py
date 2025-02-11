import os
from flask import Flask, send_file, request, render_template, redirect, url_for, flash, session
from database.db import verificacionLogin, nueva_Cuenta

app = Flask(__name__, template_folder='src')
app.secret_key = os.urandom(24) 

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/perfil")
def perfil():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('perfil.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = verificacionLogin(email, password)
        if user:
            session['user'] = user[0]
            print("Exito")
            return redirect(url_for('perfil'))
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



@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
