# bucle (infinito) que se repetirá hasta que la condición no se cumpla

contador = 0
# while > mientras
while contador < 10:
    print("Hola")
    contador += 1

print("Adios")

print("-------------")
# En los bucles (while y for) podemos termina la iteración de manera anticipada con el break
contador = 0
while contador < 100:
    print(contador)
    if contador == 10:
        break
    contador += 1