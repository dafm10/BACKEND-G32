# from LIBRERIA import CLASES ó FUNCIONES que queremos usar de la librería.
from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType
from psycopg import connect # connect > para conectarse a la base de datos
from dotenv import load_dotenv
from os import environ # os > operating systems # environ devolverá todas las variables de entorno de la máquina y aqui se agregarán las variables del archivo .env

# load_dotenv siempre debe ir en la primera linea del prouecto para que cargue todas las variables en todo el proyecto y evitar alguna variable no leida
load_dotenv()

# postgresql://NOMBRE_USUARIO:PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
credenciales = environ.get("DATABASE_URL")
conexion = connect(conninfo=credenciales)
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
        # El encargado de iniciar la comunicación con la BD
        cursor = conexion.cursor()

        # Ejecutamos el comando en la BD
        cursor.execute("SELECT * FROM productos")

        #Para obtener el resultado (si es necesario) usamos los métodos: fetchone, fecthall, fetchmany
        productos_bd = cursor.fetchall()

        print(productos_bd)

        # Finaliza la comunicación con la base de datos
        cursor.close

        resultado = []
        for producto in productos_bd:
            resultado.append({
                "id": producto[0],
                "nombre": producto[1],
                "precio": float(producto[2]),
                "cantidad": producto[3]
            })
        
        # Los controladores (es la lógica del endpoint) suelen retornar diccionarios que estos serán interpretados en JSON o también se suele retornar listas (arreglos)
        return {
            "message": "Los productos son:",
            "content": resultado
        }
    elif request.method == 'POST':
        # Se usa para crear nueva información proveniente del frontend
        # request.get_data() # retorna la información proveniente del cliente directamente como si fuese un string. Sirve también si la información enviada será un texto. No se recomienda mucho usarlo por que tenemos que volver a String y parsear para que sea un diccionario y validarlo para ver si cumple con las llaves
        # request.get_json() # retorna la información del cliente y la convierte a un diccionario pra que python la pueda entender
        print(request.get_data())
        try:
            # print(request.get_json())
            data = request.get_json()

            cursor = conexion.cursor()

            # El %s hace la conversión de la información proveniente del cliente a un String sin parámetros que puedan vulnerar mi base de datos, y ...
            # ... en los Strings comunes podemos utilizar %f para flotantes y adicionalmente el %i para convertir a enteros y podemos evitar ataques directos a la base de datos (SQL INYECTION)
            # Si queremos retornar la información que acabamos de granar en la BD, se puede utilizar el comando RETURNING columnas, es decir, si ponemos iNSERT INTO ... VALUES ... RETURNING *, esto devolverá toda la información agregada a la BD
            # https://www.psycopg.org/psycopg3/docs/basic/params.html
            cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s) RETURNING *",(
                data.get("nombre"), 
                data.get("precio"),
                data.get("cantidad")))

            # para asegurar la data y asegurarnos de que se guarde la información de manera peramente en la bd
            conexion.commit()

            # para obtener el nuevo producto creado
            nuevo_producto = cursor.fetchone()

            print(nuevo_producto)

            cursor.close()
            return {
                        "meesage": "Producto creado exitosamente"
                    }
        except UnsupportedMediaType: # Exception es la clase primordial de todos los errores
            # Handler (manejador de errores)
            return {
                "message": "Debes enviar la información en formato JSON"
            }

if __name__ == "__main__":
    # el método RUN ejecuta el servidor y lo mantiene escuchando peticiones
    app.run(port=5000, debug=True)