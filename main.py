from flask import Flask, render_template, request

import forms

app = Flask(__name__)

class Cinepolis:
    def __init__(self, nombre, num_boletos, usa_tarjeta):
        self.nombre = nombre
        self.num_boletos = num_boletos
        self.usa_tarjeta = usa_tarjeta
        self.precio_boletos = 12.00
        self.total_a_pagar = 0.0

    def calcular_descuento(self):
        if self.num_boletos > 5:
            descuento = 0.15
        elif 3 <= self.num_boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0.0

        total = self.num_boletos * self.precio_boletos
        total_con_descuento = total - (total * descuento)

        if self.usa_tarjeta:
            total_con_descuento -= total_con_descuento * 0.10

        self.total_a_pagar = total_con_descuento



@app.route("/")
def index():
    titulo = "IDGS805"
    lista = ["Pedro", "Juan", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method == 'POST':
        mat = alumno_clase.matricula.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data 
        nom = alumno_clase.nombre.data

        print('Nombre: {}'.format(nom))
    return render_template('Alumnos.html', form=alumno_clase)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/Hola")
def hola():
    return "<h1>Holaa</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numero es {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
        <form>
        <label for="nombre"> Nombre: </label>
        <input type="text" id="nombre" name="Nombre">
'''

@app.route("/OperasBas")
def operasBas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "multiplicar":
            resultado = multiplicar(num1, num2)
        elif operacion == "sumar":
            resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "dividir":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación no válida."

        return render_template("OperasBas.html", resultado=resultado)
    return render_template("OperasBas.html", resultado=None)

def multiplicar(num1, num2):
    resultado = num1 * num2
    return "La multiplicación de {} x {} es {}".format(num1, num2, resultado)

def sumar(num1, num2):
    resultado = num1 + num2
    return "La suma de {} y {} es {}".format(num1, num2, resultado)

def restar(num1, num2):
    resultado = num1 - num2
    return "La resta de {} menos {} es {}".format(num1, num2, resultado)

def dividir(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        return "La división de {} entre {} es {}".format(num1, num2, resultado)
    else:
        return "Error: No se puede dividir por cero."

@app.route('/cinepolis')
def cinepolis():
    return render_template('cinepolis.html', nombre='', compradores=None, tarjeta='No', boletos=None, total=None, error='')

@app.route('/cinepolis', methods=['POST'])
def total():
    nombre = request.form['nombre']
    compradores = int(request.form['compradores'])
    tarjeta = request.form['tarjeta']
    boletos = int(request.form['boletos'])

    num_boletos = compradores * 7

    if boletos > num_boletos:
        error = f'No puede comprar más de 7 boletos por persona. Máximo permitido: {num_boletos}.'
        return render_template('cinepolis.html', nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos, total=None, error=error)

    compra = Cinepolis(nombre, boletos, tarjeta == 'Sí')
    compra.calcular_descuento()
    total = compra.total_a_pagar

    return render_template('cinepolis.html', nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos, total=total, error='')

if __name__ == "__main__":
    app.run(debug=True, port=3000)