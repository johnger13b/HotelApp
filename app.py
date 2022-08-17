from flask import request, Flask, flash, render_template, jsonify, url_for, session, g, redirect
# from flask_login  import UserMixin, login_user, Login_Manager, login_required, logout_user, current_user
from datetime import datetime
import dB as db
from settings.config import configuracion
import forms
from forms import Habitacion, Reservas, Usuarios, profileform, admUsers
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/')
def index():
    return render_template('index.html', titulo="Ejemplo Hotel Gevora")

# ===========================================================================

@app.route('/cerrar')
def cerrar():
    flash("Sesion Cerrada")
    session.clear()
    g.user = None
    return redirect(url_for('login'))

# ===========================================================================

@app.before_request
def before_request():
    if 'username' in session:
        g.user = session['username']
    else:
        g.user = "Iniciar Sesion"

    if 'rol' in session:
        g.rol = session['rol']
    else:
        g.rol = None

# ===========================================================================

@app.route('/homeProfile')
def hprofile():
    if 'username' in session:
        print('No ingresa el usuario')
        if session['rol'] == 'Usuario' or session['rol'] == 'SuperAdministrador':
            return render_template('homeProfile.html', titulo="Ejemplo Hotel Gevora 2")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/myProfile', methods=['GET', 'POST'])
def mprofile():
    if 'username' in session:
        if session['rol'] == 'Usuario' or session['rol'] == 'SuperAdministrador':
            usuario = db.sql_select_all_usuario(g.user)
            myprofile_Form = forms.profileform(request.form)
            if request.method == 'POST':
                name = request.form["name"]
                lastname = request.form["lastname"]
                sex = request.form["sex"]
                # address = request.form["address"]
                tel = request.form["tel"]
                birddate = request.form["birddate"]
                db.sql_edit_usuario(name, lastname, g.user, tel, sex, birddate,)
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
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/admo_hab')
def admohab():
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            lista = db.sql_select_habitaciones()
            return render_template('admo_hab.html',l_hab=lista, titulo="Ejemplo Hotel Gevora 2")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/admo_hab2')
def admohab2():
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            lista = db.sql_select_habitaciones()
            return render_template('admo_hab2.html',l_hab=lista, titulo="Ejemplo Hotel Gevora 2")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/ControlHabitacion2/<string:id>', methods=['GET','POST'])
def controlHabitacion2(id):
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            acc = request.form['acc']
            valor = request.form["pre"]
            if acc == 'Eliminar':
                estado = request.form["estado"]
                idHab = id
                print(id)
                print(idHab)
                db.sql_delete_habitacion(idHab)
            elif acc == 'Actualizar':
                estado = request.form["estado"]
                idHab = id
                valor = request.form["pre"]
                db.sql_update_habitacion(idHab, estado, valor)                
            elif acc == 'Nueva Habitacion':
                lista = db.sql_select_habitaciones()
                j=1
                print (lista)
                for i in lista:
                    if j!=i[0]:
                         break
                    else:
                        j+=1
                    print(i[0])
                    print(j)
                j =str(j)
                print("id:"+j)
                db.sql_add_habitacion(j, "Disponible", valor)
        
            return redirect(url_for('admohab2'))
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/ControlHabitacion', methods=['GET','POST'])
def controlHabitacion():
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            acc = request.form['acc']
            print(acc)
            estado = request.form["estado"]
            idHab = request.form["idHab"]
            valor = request.form["pre"]
            
            if acc == 'Eliminar Habitacion':
                db.sql_delete_habitacion(idHab)
            
            elif acc == 'Actualizar':
                db.sql_update_habitacion(idHab, estado, valor)
                
            elif acc == 'Nueva Habitacion':
                lista = db.sql_select_habitaciones()
                j=1
                print (lista)
                for i in lista:
                    if j!=i[0]:
                         break
                    else:
                        j+=1
                    print(i[0])
                    print(j)
                j =str(j)
                print("id:"+j)
                db.sql_add_habitacion(j, "Disponible", valor)
        
            return admohab()
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))




# ===========================================================================

@app.route('/historialReserva')
def historeserva():
    if 'username' in session:
        if session['rol'] == 'Usuario' or session['rol'] == 'SuperAdministrador':
            print(g.user)
            reserva = db.sql_select_all_ReservaU(g.user)
            rate_Form = forms.rateform(request.form)
            flash("Lista de reservas")
            return render_template('historialReserva.html', form=rate_Form, lreservas = reserva, titulo="Historial de Reservas")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/updateRateReserva' ,methods = ['GET','POST'])
def updarerate():
    if 'username' in session:
        if session['rol'] == 'Usuario' or session['rol'] == 'SuperAdministrador':
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
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        login_Form = forms.loginForm()
        if request.method == 'POST':
            print("Entro en el Post")
            hash_password = generate_password_hash(request.form['password'], method='sha256')
            print(hash_password)
            print(request.form['password'])
            print(request.form['email'])
            username = request.form['email']
            usuario = db.sql_select_all_usuario(username)
            """  print(usuario[3]) """
            if usuario:
                result=check_password_hash(usuario[3], request.form['password'])
                if result != False:
                    session['username'] = username
                    session['rol']= usuario[7]
                    print("ingreso satisfactoriamente")
                    return redirect(url_for('index'))
                
                else:
                    flash("Invalid username or password")
            else:
                flash("Invalid username or password")

        return render_template('login.html', titulo="Ejemplo Hotel Gevora 2")       
        

# ===========================================================================

@app.route('/SignUp')
def signup():
    if 'username' in session:
        return redirect(url_for('index'))
    else:    
        form=forms.Usuarios(request.form)
        return render_template('SignUp.html', form=form, titulo="Ejemplo Hotel Gevora 2")

# ===========================================================================

@app.route('/Reservas')
def reservas():
    if 'username' in session:
        form=forms.Reservas(request.form)
        return render_template('Reservas.html', form=form, titulo="Ejemplo Hotel Gevora 2")
    else:
        return redirect(url_for('index'))

# ===========================================================================

@app.route('/Moon', methods=['GET', 'POST'])
def MoonKnight():
        if 'username' in session:
            return redirect(url_for('index'))
        else:
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
                db.sql_insert_user(Email, Nombres, Apellidos, Contraseña, FechadeNacimiento, Genero, Rol)
                flash(f"Usuario {Email} registrado correctamente")
                return render_template('login.html', titulo="Registro de nuevo producto", form = lunera)

# ===========================================================================

@app.route('/adReserva', methods=['GET', 'POST'])
def Dulcinea():
    if 'username' in session:
        Sancho = forms.Reservas(request.form)
        if request.method == 'GET':
            form = Reservas()
        if request.method == 'POST':
            print("entro al post")
            FechaInicio= request.form["birddate"]
            FechaFinal= request.form["daterbird"]
            user = session['username']
            costo= request.form["costo"]
            if g.rol == "Usuario":
                Estado="Activa"
            else:
                Estado= request.form["estado"]
            db.sql_add_reservas(FechaInicio, FechaFinal, costo, Estado, user)
            flash(f"Usuario {FechaInicio} registrado correctamente")
            return redirect(url_for('historeserva'))
    else:
        return redirect(url_for('index'))

# ===========================================================================

@app.route('/Marte', methods=['GET', 'POST'])
def Harmonia():
    Adrestia = request.form["Id"]
    db.sql_delete_reserva(Adrestia)
    
# ===========================================================================
#=====================New user===============================================

@app.route('/Vista_admin_usuarios2')
def vistaadminusuarios2():
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            l_user = db.sql_select_usuarios()
            print(l_user)
            userform= forms.admUsers(request.form)
            userformini= forms.admUsersIni(request.form)
            print("entro en el vista_admin_usuarios2")

            return render_template('vista_admin_usuarios2.html', l_users = l_user, form = userform, formini = userformini, titulo='Administacion de Usuarios')
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

# ===========================================================================

@app.route('/Controluser/<string:id>', methods=['GET', 'POST'])
def Controluser(id):
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            l_users = db.sql_select_usuarios()
            print(type(l_users))
            userform=forms.admUsers(request.form)
            userformini= forms.admUsersIni(request.form)
            if request.method == 'POST':
                hash_password = generate_password_hash('userpass123456', method='sha256')
                acc = request.form['acc']
                username = request.form['username']
                name = request.form['name']
                lastname = request.form['lastname']
                sex = request.form['sex']
                birddate = request.form['birddate']
                tel = request.form['tel']
                rol = request.form['rol']
                if acc == 'Buscar':
                    print(username)
                    if (username):
                        query = db.sql_select_usuario_all(username)
                    else:
                        query = db.sql_select_usuarios()

                    return render_template('Vista_admin_usuarios2.html', l_users = query, form = userform, formini = userformini, titulo = 'Administacion de Usuarios')
                    # return redirect(url_for('vistaadminusuarios2', l_users = query, form = userform, formini = userformini, titulo = 'Administacion de Usuarios'))
                if acc == 'Eliminar':
                    db.sql_delete_usuario(username)
                    query = db.sql_select_usuarios()
                    return render_template('Vista_admin_usuarios2.html', l_users = query, form = userform, formini = userformini, titulo = 'Administacion de Usuarios')
                elif acc == 'Actualizar':
                    print(rol)
                    db.sql_update_usuario(name, lastname, username, tel, sex, birddate, rol)
                    query = db.sql_select_usuarios()
                    return render_template('Vista_admin_usuarios2.html', l_users = query, form = userform, formini = userformini, titulo = 'Administacion de Usuarios')
                elif acc == 'Nuevo Usuario':
                    db.sql_insert_user_new(username, name, lastname, hash_password, birddate, sex, rol, tel)
                    query = db.sql_select_usuarios()
                    return render_template('Vista_admin_usuarios2.html', l_users = query, form = userform, formini = userformini, titulo = 'Administacion de Usuarios')
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))





# ==============================los siguientes son los viejos===============
# ===========================================================================

@app.route('/Vista_admin_usuarios')
def vistaadminusuarios():
    if 'username' in session:
        if session['rol'] == 'SuperAdministrador':
            return render_template('Vista_admin_usuarios.html', titulo="Ejemplo Hotel Gevora 2")
        else:
            return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))
# ===========================================================================

@app.route('/BuscarUser', methods=['GET', 'POST'])
def Buscar():
    if 'username' in session:
        Peach = forms.Usuarios(request.form)
        if request.method == 'GET':
            form = Usuarios()
        if request.method == 'POST':
            Email = request.form["email"]
            Nombres= request.form["name"]
            Apellidos= request.form["lastname"]
            Genero= request.form["sex"]
            FechaInicio= request.form["birddate"]
            FechaFinal= request.form["daterbird"]
            db.sql_insert_user(Email, Nombres, Apellidos, Genero)
            db.sql_add_reservas(FechaInicio, FechaFinal)
            flash(f"Usuario {Email} encontrado.")
            return render_template('Vista_admin_Usuarios.html', form = Peach)

# ===========================================================================

""" acc = request.form['acc']
print(acc) """

""" if acc == 'Eliminar Usuario': """
@app.route('/EliminarUser', methods=['GET', 'POST'])
def Delete():
    if 'username' in session:
         Mario = forms.Usuarios(request.form)
         if request.method == 'GET':
            form = Usuarios()
         if request.method == 'POST':
            Email = request.form["email"]
            db.sql_delete_user(Email)
            flash(f"Usuario {Email} Eliminado.")
            return render_template('Vista_admin_Usuarios.html', form = Mario)

""" if acc == 'Actualizar Usuario': """
@app.route('/EditarUser', methods=['GET', 'POST'])
def Edit():
    if 'username' in session:
        Luigi = forms.Usuarios(request.form)
        if request.method == 'GET':
            form = Usuarios()
        if request.method == 'POST':
            Email = request.form["email"]
            Nombres= request.form["name"]
            Apellidos= request.form["lastname"]
            Genero= request.form["sex"]
            FechaInicio= request.form["birddate"]
            FechaFinal= request.form["daterbird"]
            db.sql_insert_user(Email, Nombres, Apellidos, Genero)
            db.sql_add_reservas(FechaInicio, FechaFinal)
            flash(f"Usuario {Email} Actualizado.")
            return render_template('Vista_admin_Usuarios.html', form = Luigi)

app.run(debug=True)

if __name__ == '__main__':
    app.run()