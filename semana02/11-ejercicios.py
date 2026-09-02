# 1. Crea una función calcular_igv en la cual pide el precio y retorne el precio final aplicado el igv (18%) - puede utilizar lambda

def calcular_igv(precio):
    precio_con_igv = precio * 1.18
    return precio_con_igv

# Ahora con lambda (es lo mismo que la función de arriba)
calcular_igv_lambda = lambda precio: precio * 1.18

print(calcular_igv(100))
print(calcular_igv_lambda(100))

# 2. Convierte la temperatura en la función cambiar_teperatura de Celcius a Farenheit - puede utilizar lambda

def cambiar_temperatura(celcius):
    return (celcius * 9/5) + 32

cambiar_temperatura_lambda = lambda celcius: (celcius * 9/5) + 32

print(cambiar_temperatura(100))
print(cambiar_temperatura_lambda(100))


# 3. Dado un diccionario de un producto (nombre, precio, stock) utiliza if-elif para clasificar el stock en "Sin Stock" (si el stock es 0), "Stock Bajo" (si el stock es entre 1 y 10) y "Disponible" (si el stock es más que 10)

def clasificar_stock(producto):
    stock = producto.get("stock")

    if stock == 0:
        estado = "Sin Stock"
    elif 1 <= stock <= 10: # esto sirve para evitar poner: 1 <= stock and stock <= 10
        estado = "Stock Bajo"
    else:
        estado = "Disponible"
    print(f"El producto {producto.get("nombre")} tiene un estad de {estado}")

producto = {"nombre": "Ayudín", "precio": 4.5, "stock": 5}

clasificar_stock(producto)


# 4. Usando un while, simula un cjaero automático simple que pida una clave hasta que el usuario la ingrese correctamente, usando 3 intentos como máximo, si no indica que la cuenta fue bloqueada

def cajero_automatico():
    clave_correcta = "4591"
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        clave_ingresada = input("Ingresa tu clave: ")
        if clave_ingresada == clave_correcta:
            print("Bienvenido")
            break
        else:
            intentos += 1
            if intentos < max_intentos:
                print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")
    else:
        # Solamente vamos a ingresar al else si el while terminó sin un break
        print("Cuenta bloqueada por exceder el número de intentos")

cajero_automatico()

# 5. Crea una función calcular_area_circulo(radio) que retorne el área (3.1415 como valor de pi) - puede utilizar lambda

# pi * radop ** 2
pi = 3.1415
calcular_area_circulo = lambda radio: pi * (radio ** 2)
print(f"{calcular_area_circulo(10):.2f}")


# 6. Crear una función procesar_notas(nombre, *notas) que calcule y retorne el promedio y luego clasigique el resultado con if-elif-else en una segunda función clasificar(promedio)
# el * indica que se le va a pasar parámetros infinitos y se crea en una TUPLA (ordenada y no editable)

def clasificar(promedio):
    if promedio < 11:
        return "Desaprobado"
    elif 11 <= promedio < 14:
        return "Regular"
    elif 14 <= promedio < 17:
        return "Bueno"
    else:
        return "Excelente"

def procesar_notas(nombre, *notas):
    if len(notas) == 0:
        print(f"{nombre} no tiene notas registradas")
        return

    promedio = sum(notas) / len(notas)
    resultado = clasificar(promedio)
    print(f"{nombre} está {resultado}")

procesar_notas("Eduardo", 15,10,13,5)
procesar_notas("Karina", 10,20,1)
procesar_notas("David", 18)
procesar_notas("Juan")

# 7. En una lista de 5 elementos crear una función obtener_por_indice(lista, indice) que capture el error IndexError si el indice no existe

def obtener_por_indice(lista, indice):
    try:
        print(lista[indice])
    except IndexError:
        # el IndexError se emite cuando se quiere acceder a una posición inválida de una lista, tupla o diccionario
        print(f"Error: El índice {indice} no existe!")
        return

obtener_por_indice([10, 20, 30], 0)
obtener_por_indice(("a", "e", "i"), 2)
obtener_por_indice([1,2,3], 5)

# BONUS!
# 8. Crear una función con while True que pida númeeros al usuario y los sume manejando un try-except en el que caso se ingrese un texto en vez de número y que al escribir Salir, termine la sumatoria sin lanzar el error.

def sumatoria_infinita():
    suma = 0

    while True:
        entrada = input("Ingresa un número ó Salir para terminar: ")
        if entrada.lower() == "salir":
            print(f"Fin, la suma es {suma}")
            break

        try:
            numero = float(entrada)
            suma += numero
        except ValueError:
            # ValueError se da al momento de querer convertir un texto a número
            print("Entrada inválida, por favor ingresa un número o si no escribe: salir")

sumatoria_infinita()