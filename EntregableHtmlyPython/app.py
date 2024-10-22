from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import openpyxl
import os
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

# Verifica si el archivo Excel existe, si no, lo crea
EXCEL_FILE = 'database.xlsx'
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Nombre', 'Correo', 'Celular', 'Edad', 'Sexo', 'Password'])
    df.to_excel(EXCEL_FILE, index=False)


# Página principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular']
        edad = request.form['edad']
        sexo = request.form['sexo']
        password = request.form['password']

        # Hashear la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password)

        # Guardar los datos en el archivo Excel
        df = pd.read_excel(EXCEL_FILE)
        nuevo_usuario = pd.DataFrame({
            'Nombre': [nombre],
            'Correo': [correo],
            'Celular': [celular],
            'Edad': [edad],
            'Sexo': [sexo],
            'Password': [hashed_password]  # Guardamos la contraseña hasheada
        })
        df = pd.concat([df, nuevo_usuario], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)

        return redirect(url_for('index'))
    return render_template('register.html')

# Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']  # Puede ser el nombre o correo
        password = request.form['password']

        # Verificar si es el usuario administrador
        if usuario == 'adminnuevo' and password == 'admin1234':
            return redirect(url_for('admin'))

        # Si no es el admin, verificar en el archivo Excel
        df = pd.read_excel(EXCEL_FILE)

        # Buscar si el usuario existe (ya sea por nombre o correo)
        user_row = df[(df['Nombre'] == usuario) | (df['Correo'] == usuario)]

        if not user_row.empty:
            # Si el usuario existe, verificar la contraseña
            stored_password = user_row['Password'].values[0]  # Contraseña hasheada en el Excel

            if check_password_hash(stored_password, password):
                # Contraseña correcta
                return redirect(url_for('index'))
            else:
                # Contraseña incorrecta
                return "Contraseña incorrecta"
        else:
            # Usuario no encontrado
            return "Usuario no encontrado"

    return render_template('login.html')

# Página de administración
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    df = pd.read_excel(EXCEL_FILE)
    return render_template('admin.html', usuarios=df.to_dict(orient='records'))

# Página de estadísticas
@app.route('/statistics')
def statistics():
    df = pd.read_excel(EXCEL_FILE)
    
    # Contar cuántos usuarios hay de cada sexo
    count_masculino = df[df['Sexo'] == 'Masculino'].shape[0]
    count_femenino = df[df['Sexo'] == 'Femenino'].shape[0]

    # Extraer las edades
    edades = df['Edad'].tolist()

    return render_template('statistics.html', count_masculino=count_masculino, count_femenino=count_femenino, edades=edades)

# Ruta para actualizar usuario
@app.route('/update_user', methods=['POST'])
def update_user():
    nombre = request.form['nombre']
    nuevo_correo = request.form['nuevo_correo']
    nuevo_celular = request.form['nuevo_celular']

    df = pd.read_excel(EXCEL_FILE)
    df.loc[df['Nombre'] == nombre, ['Correo', 'Celular']] = nuevo_correo, nuevo_celular
    df.to_excel(EXCEL_FILE, index=False)

    return redirect(url_for('admin'))

# Ruta para eliminar usuario
@app.route('/delete_user/<nombre>', methods=['POST'])
def delete_user(nombre):
    df = pd.read_excel(EXCEL_FILE)
    df = df[df['Nombre'] != nombre]
    df.to_excel(EXCEL_FILE, index=False)

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
