from flask import Flask

"""
Para ejecutar la app de Flask necesitamos un servidor web,
Flask proporciona uno para desarrollo pero necesitamos un
par de variables de entorno.

- Linux/Max
  export FLASK_APP= hello (hello es el nombre del archivo sin
  extensión)
  export FLASK_ENV= development (puede ser también "production") 

- Windows
  set FLASK_APP = hello
  set FLASK_ENV = development

"""

app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola, soy Flask!,¿y tú?"


@app.route("/adios")
def adios():
    return "Adiós"
