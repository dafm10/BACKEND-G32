# from LIBRERIA import CLASES ó FUNCIONES que queremos usar de la librería.
from flask import Flask, request
# request > nos dará toda la información proveniente del cliente, y solamente puede ser llamado dentro de un controlador
# https://flask.palletsprojects.com/en/stable/api/#flask.Request

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se está ejecutando directamente o no en la terminal
# python3 app.py > el valor de esta variable será __main__
# python3 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ será secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patron de diseño de SINGLETON
app = Flask(__name__)

productos = [
    {
        "id":1,
        "nombre": "Vaso de vidrio"
    }, 
    {
        "id":2, 
        "nombre": "Parlante"
    },
    {
     "id": 3,
     "nombre": "Botella de agua"
    }]

# Cada ruta (endpoint) Punto Final (punto de acceso)
@app.route('/estado')
def estado_servidor():
    # Es de suma importancia que siempre en los endpoints retornemos algo
    return 'El servidor está vivo!'

# si no se declara el parámetro METHODS, su valor por defecto será 'GET'
@app.route('/productos', methods = ['GET', 'POST'])
def gestionar_productos():
    print(request.method)
    if request.method == 'GET':
    # Los controladores (es la lógica del endpoint) suelen retornar diccionarios que estos serán interpretados en JSON o también se suele retornar listas (arreglos)
        return {
            "message": "Los productos son:",
            "content": productos
        }
    elif request.method == 'POST':
        return {
            "meesage": "Producto creado exitosamente"
        }

if __name__ == "__main__":
    # el método RUN ejecuta el servidor y lo mantiene escuchando peticiones
    app.run(port=5000, debug=True)