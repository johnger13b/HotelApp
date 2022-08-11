from flask import request, Flask,flash, render_template, jsonify, url_for
import flask
import crudHabitacion as bd
from settings.config import configuracion
import sqlite3
from sqlite3 import Error
from forms import Habitacion

app = Flask(__name__)
app.config.from_object(configuracion)


@app.route('/')
def index():
    return render_template('index.html', titulo="Ejemplo Hotel Gevora")

@app.route('/homeProfile')
def hprofile():
    return render_template('homeProfile.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/myProfile')
def mprofile():
    return render_template('myprofile.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/admo_hab')
def admohab():
    lista = bd.sql_select_habitaciones()
    print(lista)
    
    return render_template('admo_hab.html',l_hab=lista, titulo="Ejemplo Hotel Gevora 2")

@app.route('/historialReserva')
def historeserva():
    return render_template('historialReserva.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Hotel Gevora")

@app.route('/SignUp')
def signup():
    return render_template('SignUp.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/Vista_admin_usuarios')
def vistaadminusuarios():
    return render_template('Vista_admin_usuarios.html', titulo="Ejemplo Hotel Gevora 2")

@app.route('/ControlHabitacion', methods=['GET','POST'])
def controlHabitacion():
    acc = request.args.get["acc"]
    estado = request.args.get["estado"]
    idHab = request.args.get["idHab"]
    
    if acc == 'Eliminar+Habitacion':
        bd.sql_delete_habitacion(idHab)
        return render_template('admo_hab.html', titulo="Ejemplo Hotel Gevora 2")
    else:
        # bd.sql_update_habitacion(idHab, estado)
        return render_template('admo_hab.html', titulo="Ejemplo Hotel Gevora 2")
 

app.run(debug=True)







