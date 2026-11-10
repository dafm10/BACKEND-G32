# https://docs.docker.com/reference/dockerfile/
# FROM desde que imagen vamos a partir
FROM python:3.14-slim

# ENV configuramos variables de entorno en el contenedor
# Si se quiere continuar escribiendo en las lineas continuas sin importar el enter podemos colocar un \
# PYTHONDONTWRITEBYTECODE = Evita que python cree archivos .pyv y carpetas __pycache__
# PYTHONUNBUFFERED = Desactiva el bufer de salida de python ya que con el bufer activo python acumula los prints y logs antes de enviarlos, en cambio si se desactiva los mensajes salen de inmediato
ENV PYTHONDONTWRITEBYTECODE=1 \ 
    PYTHONUNBUFFERED=1


# Creamos el directorio de trabajo
# Esto creará en el contenedor una carpeta donde se almacenará todos los archivos del proyecto y no interferirá con la imagen usada como base
WORKDIR /app

# Copia el archivo/directorio indicado en la ubicación seleccionada
COPY requirements.txt .

# Instalamos las librerias necesarias para el proyecto antes de crear el usuario
RUN pip install -r requirements.txt

# Copiar todos los archivos en el directorio base
COPY . .

# RUN > sirve para ejecutar un comando en la terminal del contenedor
# useradd > crea un nuevo usuario en mi contenedor: app
# chown -R app:app / app > Entrega las carpetas /app para que el usuario las pueda visualizar
# && > sirve para ejecutar otro comando cuando el primero se ejecutó de manera exitosa
# RUN useradd -m app && chown -R app:app /app
RUN useradd -m david && chown -R david:david /app

# Ahora asignamos el usuario que va a utilizar la aplicación
# USER app
USER david


# Mi contenedor podrá ser accedido desde fuera mediante un puerto expuesto, en este caso el 8000
EXPOSE 8000