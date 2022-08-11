from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Habitacion(FlaskForm):
    idHab = StringField('idHab', validators=[DataRequired()])
    acc = StringField('acc', validators=[DataRequired()])
    estado = StringField('estado', validators=[DataRequired()])
