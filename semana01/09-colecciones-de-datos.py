# Listas (Arreglos)

# las listas se representan con corchetes []
# Colección de datos ordenada y editable
frutas = ['manzana', 'pera', 'kiwi', 'plátano']

# ordenada > accedemos a su contenido por sus posiciones que inician desde cero (0)
print(frutas[0])

# se puede recorres las listas tanto de izquierda a derecha como viceversa
print(frutas[-1])

# puedo sacar una sub-lista
print(frutas[1:3])

# si no se le pone posición inicial, mostrará desde el comienzo
print(frutas[:3])

# si no se le pone posición final, mostrará hasta el ultimo item
print(frutas[3:])

# LOS MÉTODOS MAS USADOS DE LAS LISTAS
# append > agregamos nuevos elementos al final de la lista
frutas.append('sandía')

# insert > inserta el elemento en la posición deseada
frutas.insert(1, 'mango')
print(frutas)

# remove > elimna el valor si lo encuentra, y si no hay lanzará un error
# frutas.remove(1)

# pop > elimina el contenido por su indice y devuelve el valor eliminado
eliminado = frutas.pop(5)
print(eliminado)
#opcionalmente, el pop si no le pasamos el indice, elimina el último item de la lista

# sort > ordena alfabeticamente los elementos de la lista, solamente funciona si todos los elementos de la lista son string
frutas.sort()
print(frutas)

# reverse > invierte el orden actual
frutas.reverse()
print(frutas)

# lean devuelve la cantidad de elementos que hay en una lista
longitud = len(frutas)
print(longitud)

# Clear > limpia toda la lista y la deja vacía
frutas.clear()
print(frutas)