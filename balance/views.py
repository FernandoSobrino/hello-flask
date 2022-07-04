from balance import app

@app.route('/')
def home():
    return "Página de inicio"

@app.route('/nuevo')
def nuevo_movimiento():
    return "Has creado un movimiento nuevo"

@app.route('/modificar')
def actualizar():
    return "Has actualizado el movimiento"

@app.route('/borrar')
def borrar():
    return "Has borrado un movimiento"
