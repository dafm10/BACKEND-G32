# Tenemos un número que adivinar, entonces pedir al usuario que ingrese un número entre el 1 y el 10 hasta que lo adivine, una vez que lo adivine indícale "GANASTEEE" y terminar el WHILE, use break
secreto = 10

# La condición siempre va a ser verdadera (bucle infinito)
# while True:
#     num = int(input("Ingresa un número entre 1 y 20: "))
#     if num == secreto:
#         print("Ganasteeee")
#         break

# no_adivino = True
# while no_adivino:
#     num = int(input("Ingresa un número entre 1 y 20: "))
#     if num == secreto:
#         print("Ganasteeee!")
#         # no_adivino = False
#         break
#     else:
#         print("Sigue intentado")


# Ingresar 5 precios a la lista y si se ingresa un valor negativo ó 0 no se debe de tomar en consideración
lista_precios = []
# NO USAR BREAK, SOLO CONTINUE

# while len(lista_precios) < 5:
#     num = int(input("Ingresa un número: "))
#     if num > 0:
#         lista_precios.append(num)
#         continue
#     else:
#         print("Ingresa un número mayor a 0")

# print(lista_precios)

while len(lista_precios) < 5:
    precio = int(input("Ingresa el precio: "))
    if precio <= 0:
        print("El precio no puede ser negativo")
        continue
    lista_precios.append(precio)

print(lista_precios)