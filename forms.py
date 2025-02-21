from wtforms import Form, StringField, EmailField
from wtforms.validators import DataRequired, Length, Email

class UserForm(Form):
    matricula = StringField('Matricula', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=10, message='El campo debe tener entre 3 y 10 caracteres')
    ])
    nombre = StringField('Nombre', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=50, message='El campo debe tener entre 3 y 50 caracteres')
    ])
    apellido = StringField('apellido', [
        DataRequired(message='El campo es requerido'),
        Length(min=3, max=50, message='El campo debe tener entre 3 y 50 caracteres')
    ])
    email = EmailField('Correo', [
        DataRequired(message='El campo es requerido'),
        Email(message='Correo electrónico no válido')
    ])



    



