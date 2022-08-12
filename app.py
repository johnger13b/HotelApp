from flask import request, Flask,flash, render_template, jsonify, url_for, session, g
from datetime import datetime
import crudHabitacion as bd
import dB as db
from settings.config import configuracion
import sqlite3
from sqlite3 import Error
import forms
from forms import Habitacion, Usuarios
from forms import profileform
import dB as diana
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/')
def index():
    session['username'] = 'cway@oulook.com'
    session['rol']= 'Administrador'
    return render_template('index.html', titulo="Ejemplo Hotel Gevora")


@app.route('/cerrar')
def cerrar():
    flash("Sesion Cerrada")
    session.clear()
    g.user = None
    return render_template('index.html')

@app.before_request
def before_request():
    if 'username' in session:
        g.user = 'cway@outlook.com'
    else:
        g.user = None

    if 'rol' in session:
        g.rol = 'Administrador'
    else:
        g.rol = None

@app.route('/homeProfile')
def hprofile():
    return render_template('homeProfile.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/myProfile', methods=['GET', 'POST'])
def mprofile():
    
    usuario = db.sql_select_all_usuario(g.user)
    myprofile_Form = forms.profileform(request.form)
    if request.method == 'POST':
        name = request.form["name"]
        lastname = request.form["lastname"]
        sex = request.form["sex"]
        # address = request.form["address"]
        tel = request.form["tel"]
        birddate = request.form["birddate"]
        db.sql_edit_usuario(name, lastname, g.user, tel, sex, birddate)
        flash('Actualizado con exito!')       
        return render_template('myprofile.html', titulo="Ejemplo Hotel Gevora 2", form = myprofile_Form)
    elif request.method == 'GET':
        if usuario:
            myprofile_Form.name.data = usuario[1]
            myprofile_Form.lastname.data = usuario[2]
            myprofile_Form.sex.data = usuario[5]
            # myprofile_Form.address.data = usuario[1]
            myprofile_Form.username.data = usuario[0]
            myprofile_Form.tel.data = usuario[6]
            myprofile_Form.birddate.data = datetime.strptime(usuario[4],'%Y-%m-%d').date()
           
        else:
             flash('No hay Usuarios Registrados!')

        return render_template('myprofile.html',form=myprofile_Form, titulo="Mi Perfil")

@app.route('/admo_hab')
def admohab():
    lista = bd.sql_select_habitaciones()
    print(lista)
    return render_template('admo_hab.html',l_hab=lista, titulo="Ejemplo Hotel Gevora 2")

@app.route('/historialReserva')
def historeserva():
    reserva = db.sql_select_all_ReservaU(g.user)
    rate_Form = forms.rateform(request.form)
    # if request.method == 'POST':
    #     idReserva = request.form["IdReserva"]
    #     rate = request.form["rate"]
    #     comentario =  request.form["comentario"]

    #     if idReserva:
    #         db.sql_edit_rate_reserva(idReserva, rate, comentario)
    # if request.method == 'GET':
    flash("Lista de reservas")
    return render_template('historialReserva.html', form=rate_Form, lreservas = reserva, titulo="Historial de Reservas")

@app.route('/updateRateReserva' ,methods = ['GET','POST'])
def updarerate():
    reserva = db.sql_select_all_ReservaU(g.user)
    rate_Form = forms.rateform(request.form)
    if request.method == 'POST':
        idReserva = request.form["IdReserva"]
        rate = request.form["rate"]
        comentario =  request.form["comentario"]
        if idReserva:
            db.sql_edit_rate_reserva(idReserva, rate, comentario)

    if request.method == 'GET':
        flash("Lista de reservas")

    # return render_template('historialReserva.html', form=rate_Form, lreservas = reserva, titulo="Historial de Reservas")
    return historeserva()

@app.route('/login')
def loginfor():
    login_Form = forms.loginForm()
    hash_password = generate_password_hash(request.form['password'], method='sha256')
    username= request.form['username']
    new_user = usuario(username, hash_password)    
    return render_template('login.html', titulo="Ejemplo Hotel Gevora 2", form = login_Form)

@app.route('/SignUp')
def signup():
    form=forms.Usuarios(request.form)
    return render_template('SignUp.html', form=form, titulo="Ejemplo Hotel Gevora 2")

@app.route('/Vista_admin_usuarios')
def vistaadminusuarios():
    return render_template('Vista_admin_usuarios.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/ControlHabitacion', methods=['GET','POST'])
def controlHabitacion():
    acc = request.args.get('acc')
    print(acc)
    estado = request.args.get("estado")
    idHab = request.args.get("idHab")
    
    if acc == 'Eliminar Habitacion':
        bd.sql_delete_habitacion(idHab)
       
    elif acc == 'Actualizar':
        bd.sql_update_habitacion(idHab, estado)
        
    elif acc == 'Nueva Habitacion':
        lista = bd.sql_select_habitaciones()
        j=0
        for i in lista:
            j+=1
            if j!=i[0]:
                break
                # break
            print(i[0])
        j =str(j)
        bd.sql_add_habitacion(j, "Disponible")
  
    return admohab()

@app.route('/Moon', methods=['GET', 'POST'])
def MoonKnight():
    lunera = forms.Usuarios(request.form)
    if request.method == 'GET':
        form = Usuarios()
    if request.method == 'POST':
        Email= request.form["email"]
        Nombres= request.form["name"]
        Apellidos= request.form["lastname"]
        hash_password = generate_password_hash(request.form["contra"], method='sha256')
        Contraseña= hash_password
        FechadeNacimiento= request.form["birddate"]
        Genero= request.form["sex"]
        Rol= request.form["rol"]
        diana.mardeluna(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol)
        flash(f"Usuario {Email} registrado correctamente")
        return render_template('login.html', titulo="Registro de nuevo producto", form = lunera)

app.run(debug=True)