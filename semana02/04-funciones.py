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
    return {
        "dolar_compra": dolar_compra,
        "dolar_venta": dolar_venta,
    }  # luego de poner la palabra return, no podemos escribir más código dentro de la función


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
    # Si en una función se manda a llamar al print pero no se retorna nada, se imprimirá en la terminal pero no habrá nada que retornar
    print(num1 + num2)


resultado = sumar(10, 5)
print(resultado)

print("--------------------------------------")
# EJERCICIOS
# 1. Crear una función calcular_area_rectangulo(base, altura) e imprima el resultado (base * altura)


def calcular_area_rectangulo(b: float, h: float):
    resultado = b * h
    print(f"El área del rectángulo es {resultado}")

calcular_area_rectangulo(10,2)
calcular_area_rectangulo(20,4)
calcular_area_rectangulo(15,7)


# 2. Crear una función es_par(numero) y que retorne si es par o impar (usando el %)


def es_par(num: int):
    return "El número es par" if num % 2 == 0 else "El número es impar"

print(es_par(6))

# 3. Dado una lista de diccionarios de productos, crear una función mostrar_info(producto) y que retorne el string: "Hay {stock} unidades del producto {nombre}"
productos = [
    {"nombre": "Tomatodo 500ml", "stock": 20},
    {"nombre": "Ventilador", "stock": 50},
    {"nombre": "Parlante Bluetooth", "stock": 25},
    {"nombre": "Café en grano 500gr", "stock": 100},
]


# Pasando producto por producto a la función
def mostrar_info(producto):
    return f"Hay {producto.get("stock")} unidades del producto {producto.get("nombre")}"

for p in productos:
    print(mostrar_info(p))


# Pasando todos los productos a la función e internamente los iteramos
def mostrar_info_todos(productos):
    for producto in productos:
        print(f"Hay {producto.get("stock")} unidades del producto {producto.get("nombre")}")

mostrar_info_todos(productos)

print("===========")
# Se necesita buscar en la lista de productos, el stock de determinado producto, si no lo encuentra, indicar que el producto no existe.
def mostrar_stock_prpducto(nombre):
    for producto in productos:
        # al momento de buscar convertimos los valores del diccionario como el valor a buscar, todo a minuscula
        if producto.get("nombre").lower() == nombre.lower():
            return f"Hay {producto.get("stock")} unidades"
    return "El producto no existe"

nombre = input("Ingresa el nombre del producto a buscar: ")
print(mostrar_stock_prpducto(nombre))