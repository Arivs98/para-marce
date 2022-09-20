from flask import Flask, request, url_for, redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/proyecto.db'
db = SQLAlchemy(app)
class Alumno(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    numero = db.Column(db.Integer)
    ciudad = db.Column(db.String)
    departamento = db.Column(db.String)
    modalidad = db.Column(db.String)
    eleccion = db.Column(db.String)
class Maestro(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    numero = db.Column(db.Integer)
    ciudad = db.Column(db.String)
    departamento = db.Column(db.String)
    modalidad = db.Column(db.String)
    eleccion = db.Column(db.String)
    

@app.route("/formulario")
def admin():
    return render_template("formulario.html")


@app.route("/data", methods= ['POST']) #metodo post es el que perimete el guardado de los datos en la BD
def carga():
    intento_de_leer = request.form['eleccion']
    if intento_de_leer=="2":
        tarea = Alumno(
        nombre=request.form['nombre'],
        apellido=request.form['apellido'],
        numero=request.form['numero'],
        ciudad=request.form['ciudad'],
        departamento=request.form['departamento'],
        modalidad=request.form['tecnica'],
        eleccion=request.form['eleccion'] #CAMBIAR VARIABLE A MODALIDAD
        )
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('admin'))
    elif intento_de_leer=="1":
        tarea = Maestro(
        nombre=request.form['nombre'],
        apellido=request.form['apellido'],
        numero=request.form['numero'],
        ciudad=request.form['ciudad'],
        departamento=request.form['departamento'],
        modalidad=request.form['tecnica'],
        eleccion=request.form['eleccion'] #CAMBIAR VARIABLE A MODALIDAD
        )
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('admin'))
    

    
if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/tarjetas')
def tarjeta():
    maestros = Maestro.query.all()
    return render_template('lista_de_artesanos', maestros=maestros)