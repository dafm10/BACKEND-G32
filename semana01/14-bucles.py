# FOR plano (sin el uso de ninguna colección de datos)
# range(x,y,z)
# Si solo utilizamos un parámetro
# X es el tope, es decir hasta que número va a incrementar menor que desde 0
# Y es el inicio, es decir desde que número va a empezar
# Z es el modificar, es decir de cuanto en cuanto se va a incrementer o decrementar, su valor por defecto es 1
# siempre cuando queremos que empiece el for le ponemos ":"

for numero in range(10):
    None  # Si aun no sabemos que hacer en este bloque de código, podemos usar el None

for numero in range(10):
    print(numero)

# En python no se puede poner bloques de código tabulados si no están precedidos por un estatuto de identación (for)
print("hola")
print("uf, trerminé")

for numero in range(5, 10):
    print(numero)

for numero in range(5, 10, 2):
    print(numero)

print("----------------------")
# Los FOT son más útiles dentro de las colecciones de datos por que puedo iterar y navegar por cada uno de sus elementos
# Todas las colecciones de datos son iterables

numeros = [10, 15, 7, 20, 13, 9]

for x in numeros:
    print(x)
