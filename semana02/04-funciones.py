# Una función es un bloque de código que se puede repetir las veces que sea necesario
# una función se declara con DEF (definición) al inicio
def saludar():
    print("Hola, soy una función")

# Declara la funcion: definir su contenido

# Invocar a la función: llamar para ejecutar su contenido
saludar()

# Si en mis funciones aún no tengo la lógica definida, puedo usar PASS, esto tambien sirve para los bloques de código como IF-ELSE, FOR, WHILE
def calcular_promedio():
    pass

# en python se recomienda usar tanto en funciones como en nombre de variables el SNAKE_CASE
# 3 tipos de convención de escribir: snake_case, CamelCase, pascalCase

# pueden retornar información
def obtener_tipo_cambio():
    # supongamos que consumimos una API
    dolar_compra = 3.31
    dolar_venta = 3.48
    return {"dolar_compra": dolar_compra, "dolar_venta": dolar_venta} # luego de poner la palabra return, no podemos escribir más código dentro de la función

resultado = obtener_tipo_cambio()

print(resultado)

# Podemos pasar parámetros sin indicar el tipo de dato, PERO en las últimas versiones se puede indicar el tipo pero no es restringido
# declarar el tipo de dato, nos ayuda a documentar mejor nuestro proyecto
def saludo_personalizado(nombre: str):
    """Funcion que sirve para devolver un saludo en bae al nombre"""
    # DOCUMENTACIÓN DE LAS FUNCIONES > esto va siempre al comienzo
    return f"Bienvenido {nombre}"

print(saludo_personalizado("David"))


def presentacion(nombre: str, edad: int, ciudad: str):
    return f"Hola, me llamo {nombre}, tengo {edad} años y soy de {ciudad}"

# El orden que le pongamos a los parámetros IMPORTA
print(presentacion("David", 38, "Trujillo"))
print(presentacion("Pepe", 50, "Lima"))
print(presentacion("Lucha", 25, "Jaén"))

# Si queremos modificar el orden de los parámetros
print(presentacion(ciudad="Cuzco", nombre="Rouse", edad=33))


def sumar(num1, num2):
    print(num1 + num2)

resultado = sumar(10,5)
print(resultado)