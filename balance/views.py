from flask import render_template

from balance import app
from .models import ListaMovimientos


@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/nuevo')
def nuevo_movimiento():
    return "Has creado un movimiento nuevo"


@app.route('/modificar')
def actualizar():
    return "Has actualizado el movimiento"


@app.route('/borrar')
def borrar():
    return "Has borrado un movimiento"
