# 1. Crear una lista de 5 productos, luego agregar uno nuevo, eliminar el 2do producto y ordenar alfabeticamente los productos e imprimirlos

miLista = ['TV', 'PC', 'Notebook', 'Radio', 'PS5']
miLista.append('iPhone')
miLista.pop(1)
miLista.sort()
print(f'Lista ordenada: {miLista}')

# 2. Tengo la siguiente lista (matriz)
matriz = [[1,2], [3,4]]
# Cómo hago para obtener el '3
print(matriz[1][0])