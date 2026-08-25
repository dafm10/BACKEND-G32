edad = 20

if edad >= 18:
    print("Puedes ingresar a la pagina")
    # tambien se puede agregar un escenario en el cual no se cumpla la condición
else:
    print('Ve a google')

# lo que se coloque fuera del bloque de identación siempre se va a ejecutar
print("Gracias por usar el programa")



# pedir un numero por teclado, convertir ese numero a int y ver si el numero es positivo SOLO SI ES MAYOR QUE 0

number = int(input("Ingresa un número: "))
if number > 0:
    print("El número es positivo")
else:
    print("El número es negativo")