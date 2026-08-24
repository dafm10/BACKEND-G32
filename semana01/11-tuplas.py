# es una colección de datos que es ordenada pero NO es editable
# una vez que se crea, ya no se puede moodificar
# sirve para guardar variables de valor que no se van a mover
# no suelen guardar mucha información

persona = ("Eduardo", 30, "Arequipa")

print(persona[0])

# Puedo desempaquetar los datos en variables independientes
nombre, edad, ciudad = persona

#CUIDADO AL CREAR LAS TUPLAS DE UN SOLO ELEMENTO
numeros = (1)
# cuando se crea una tupla de un solo elemento y este no tiene una coma al final, los parénetesis representantes de la tupla no son considerados y al final se eliminan
print(type(numeros)) # el tipo de dato sería "int"

numeros = (1,)
print(type(numeros)) # el tipo de dato sería "tuple"