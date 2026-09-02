# En el case que se reciba una cantidad indeterminada de parámetro usamos el "*args" (arguments)
def promedio_notas(*notas):
    # el parámetro * es una tupla que nunca la voy a poder editar
    print(notas)
    # quiero sacar el promedio de todas las notas
    # Método 1: usando función sum
    promedio = sum(notas) / len(notas) # esta forma seria la mas adecuada para sacar el promedio
    print(promedio)

    # Método 2: usando for e incrementadores
    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    print(promedio)

# al pasarle los parámetros serán con ","
promedio_notas(15, 20, 6, 12, 8.5)
promedio_notas(15, 20, 8.5)
promedio_notas(13, 10)
promedio_notas(15, 6, 8)


# Se puede también combinar el parámetro con los *args
# Solo se puede colocar un parámetro luego de los *args
# Para el tipado de una colección de datos, si queremos indicar que todos los elementos van a ser int, entonces [int,...]
# Si queremos indicar que la tupla va a tener SOLO 2 ELEMENTOS y esos van a ser int y str, entonces [int, str]
# tuple > tupla
# dict > diccionario
# list > lista
# object > conjunto
def promedio_notas_alumno(nombre:str, *notas: tuple[int,...]):
    print(nombre)
    print(notas)

promedio_notas_alumno("Eduardo", 10, 20, 5)