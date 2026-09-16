# EJERCICIO 4
# Crea una funcion llamada clasificar_nota(nota) que reciba una nota
# del 0 al 20 y retorne (usando if-elif-else):

# * "Excelente" si la nota es entre 17 y 20
# * "Bueno" si la nota es entre 14 y 16
# * "Regular" si la nota es entre 11 y 13
# * "Desaprobado" si la nota es menor a 11
# Luego, prueba la funcion con al menos 4 notas diferentes e imprime
# los resultados.

def clasificar_nota(nota):
    if 17 <= nota <= 20:
        return "Excelente"
    elif 14 <= nota <= 16:
        return "Bueno"
    elif 11 <= nota <= 13:
        return "Regular"
    else:
         return "Desaprobado"


print(clasificar_nota(18))
print(clasificar_nota(15))
print(clasificar_nota(12))
print(clasificar_nota(10))



# EJERCICIO 5
# Crea una funcion llamada calcular_promedio(*notas) que reciba una cantidad indeterminada de notas (usando *args), calcule el promedio y luego llame internamente a la funcion clasificar_nota del ejercicio anterior para mostrar el resultado final en pantalla con un mensaje como: "El promedio es 15.5 y la clasificacion es Bueno".

promedio = 0

def calcular_promedio(*notas):
    promedio = sum(notas) / len(notas)
    print(f"El promedio es {promedio} y la clasificación es {clasificar_nota(promedio)}")


calcular_promedio(15, 12, 16, 20, 18, 13)
calcular_promedio(10, 11, 12, 13, 8, 11)