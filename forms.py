from flask_wtf import Form, FlaskForm
from wtforms.fields import DateField
from wtforms import StringField,  PasswordField, SubmitField, SelectField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired

class Habitacion(FlaskForm):
    idHab = StringField('idHab', validators=[DataRequired()])
    acc = StringField('acc', validators=[DataRequired()])
    estado = StringField('estado', validators=[DataRequired()])
    
class loginForm(Form):
    username = EmailField('username', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    send = SubmitField('Ingresar')

class profileform(Form):
    name = StringField('Nombres:', validators=[DataRequired()])
    lastname = StringField('Apellidos:', validators=[DataRequired()])
    sex = SelectField('Sexo:', choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], validators=[DataRequired()])
    address = StringField('Direccion:', validators=[DataRequired()])
    tel = StringField('Telefono:', validators=[DataRequired()])
    birddate = DateField('Fecha de nacimiento:', validators=[DataRequired()])
    username = EmailField('Correo:', validators=[DataRequired()])
    contra = PasswordField('Contraseña')
    send = SubmitField('Actualizar')

class rateform(Form):
    IdReserva = StringField('IdReserva', validators=[DataRequired()])
    rate = StringField('Rate', validators=[DataRequired()])
    comentario = StringField('Comentario:', validators=[DataRequired()])
    send = SubmitField('Guardar')