print("---- EJERCICIO 1 ----")
# 1. Dado la lista números = [4,8,15,16,23,42] Usando un for calcula la suma total

numeros = [4, 8, 15, 16, 23, 42]
suma = 0

for numero in numeros:
    suma += numero

print(f"La suma es {suma}")

print("")
print("---- EJERCICIO 2 ----")
# 2. Dado la lista de nombres = ["Joshua", "Judith", "Eduardo", "Jean Pierre", "Luis"], quiero convertir todos los nombres a mayúscula (.upper())

nombres = ["Joshua", "Judith", "Eduardo", "Jean Pierre", "Luis"]
# nombres_mayus = []

print("Los nombres en mayúscula son:", end=' ')
for nombre in nombres:
    print(nombre.upper(),end=', ')
    # nombres_mayus.append(nombre.upper())

print(" ")
# print(nombres_mayus)


print(" ")
print("---- EJERCICIO 3 ----")
# 3. Dado la lista de precios = [10.5, 14.8, 17.2, 19.45]. Calcular el promedio y la cantidad de elementos de la lista

precios = [10.5, 14.8, 17.2, 19.45]
suma = 0
promedio = 0

for precio in precios:
    suma += precio

promedio = suma / len(precios)
# si una vatiable flotante queremos limitar sus decimales usamos :.nf
print(f'el promedio es {promedio:.2f}')

print(" ")
print("---- EJERCICIO 4 ----")
# 4. Tengo la siguiente lista de TUPLAS estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo", 18), ("Fátima", 23)], usando un FOR desempaquete la tupla e imprime usando el formato "NOMBRE tiene EDAD años

estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo", 18), ("Fátima", 23)]

for estudiante in estudiantes:
    print(f'El estudiante {estudiante[0]} tiene {estudiante[1]} años')

print(" ")
print("DESTRUCTURACIÓN DE DATOS de la tupla")
for nombre, edad in estudiantes:
    print(f'El estudiante {nombre} tiene {edad} años')


print(" ")
print("---- EJERCICIO 5 ----")
# 5. Tengo el diccionario

producto = {
    "nombre": "Tarjeta Gráfica",
    "precio": 3020.52,
    "especificaciones": "Tarjeta gráfica de última generación",
    "pros": ["Económica", "Moderna", "Sencilla instalación"],
    "contras": ["No hay garantía", "Se sobrecalienta", "No tiene drivers"],
    "info_adicional": {"pais_procedencia": "China", "estado": "Nuevo", "caja": False},
}
# Necesito saber cuantos pros y contras tenngo, asi mismo quiero saber que pais_procedencia es y cual es el último contras

print(f'Estos son los pros: {", ".join(producto["pros"])}') # usamos join para quitar los []
print(f'Estos son los contras: {", ".join(producto["contras"])}')
print(f'El pais de procedencia es: {producto["info_adicional"]["pais_procedencia"]}')
print(f'El ultimo contra es: {producto["contras"][-1]}')


print(" ")
print("---- EJERCICIO 6 ----")
# 6. Tengo una lista de tuplas ventas = [("enero", 1500), ("Febrero", 2300), ("Marzo", 1800)], recórrela en un FOR y construye un diccionario ventas_dic donde la clave sea el mes y el valor sea el monto. Es decir, el resultado final debe ser:
# ventas_dic = ["enero": 1500, "febrero":2300, "marzo": 1800]

ventas = [("enero", 1500), ("Febrero", 2300), ("Marzo", 1800)]
ventas_dic = {}

for mes, monto in ventas:
    ventas_dic[mes] = monto

print(ventas_dic)

print(" ")
print('Otra forma de mostrar')
for elemento in ventas_dic:
    print(f'{elemento}: {ventas_dic[elemento]}')

print(" ")
print('Otra forma de mostrar')
# .items() devuelve los elementos del diccionario en una tupla en la cual la primera posición es el elemento y la segunda es el valor y por ende se hace una destructuración
for elemento, valor in ventas_dic.items():
    print(f'{elemento}: {valor}')