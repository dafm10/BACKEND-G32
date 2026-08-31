# SCOPE (Alcance) como puedo utilizar mis variables dentro de las funciones

def calcular():
    resultado = 100
    print(resultado)

calcular()
# La variable resultado solo existe dentro de la función
# print(resultado)

# Las variables globales (que no están dentro de la función) si pueden ser leídas dentro de la función

nombre = "David"
def mostrar():
    # Si "modificamos" una variable global, no se modificará, sino lo que se hará es que se creará otra variable local dentro de la función con el mismo nombre pero en una posición de memoria diferente
    nombre = "Juanito"
    # la función "id" es una función de python que sirve para retornar el identificador único de esa variable
    print(id(nombre))
    print(nombre)

mostrar()
print(id(nombre))
print(nombre)

contador = 0

# def incrementar():
#     # como modificamos la variable, entonces se crea una nueva, pero al incrementar en 1 el valor inicial no existe
#     contador += 1

# incrementar()

# NO HAY QUE ABUSAR DE ESTO! (Es una mala práctica por que podemos malograr el ciclo de la variable (alterar su resultado sin que nos demos cuenta))
def incrementar():
    # al querer utilizar una variable global para modificarla dentro de la función, usamos la palabra reservada "global
    global contador
    contador += 1
    # return contador

# print(incrementar())
incrementar()
print(contador)

# la forma correcta de evitar el uso de "global"
contador = 0
def incrementar_en_uno(valor):
    return valor + 1

contador = incrementar_en_uno(contador)
print(contador)