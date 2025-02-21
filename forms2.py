from wtforms import Form, StringField, DateField, RadioField
from wtforms.validators import DataRequired, Length

class UserForm2(Form):
    nombre = StringField('Nombre', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=50, message='El campo debe tener entre 3 y 50 caracteres')
    ])
    apellidoP = StringField('Apellido Paterno', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=50, message='El campo debe tener entre 3 y 50 caracteres')
    ])
    apellidoM = StringField('Apellido Materno', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=50, message='El campo debe tener entre 3 y 50 caracteres')
    ])
    fecha_nacimiento = DateField('Fecha de Nacimiento', [
        DataRequired(message='El campo es requerido')
    ])
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')], validators=[DataRequired()])
