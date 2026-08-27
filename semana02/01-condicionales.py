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


# Se necesita registrar la venta por teclado y si la venta es mayor o igual a 100 soles entonces agregar un descuento del 10%, caso contrario no agregar descuento, y luego mostrar cuanto debe de pagar.

importe = float(input("Ingresa el importe a pagar: "))
precio_final = 0

if importe >= 100:
    precio_final = importe - (importe * 0.10)
    print(f"El total a pagar es: {precio_final}, y se aplicó un dscto. del 10%")
else:
    print(f"El total a pagar es: {importe}")



# OPERADOR TERNARIO
# Se usa si en el if-else solo vamos a tener una sola línea de código
# variable = RESULTADO_SI_ES_VERDADERA if CONDICION else RESULTADO_SI_NO_ES_VERDADERA
precio_final = importe * 0.9 if importe >= 100 else importe


print("---- EJERCICIO ----")
# Usando el operador ternario, indicar si el número es par o impar

num = int(input("Ingresa un número: "))

# print('es par') if num % 2 == 0 else print('es impar')
resultado = "Par" if num % 2 == 0 else "impar"
print(f'El número es {resultado}')



# ---------- IF ANIDADOS ----------
# si su nota es entre 90 y 100 es excelente, si su nota es entre 70 y 90 es bueno, si su nota es entre 50 y 70 es regular y si es menor que 50 es malo

nota = 60

if nota >= 90 and nota <= 100:
    print("Es excelente")
elif nota >= 70 and nota < 90:
    print("Es bueno")
elif nota >= 50 and nota < 70:
    print("Es regular")
else:
    print("Es malo")



nacionalidad = ""

if nacionalidad == "PERUANO":
    print('Que rico es el ceviche')
elif nacionalidad == "BOLIVIANO":
    print('Que rico es la salteña')
elif nacionalidad == "COLOMBIANO":
    print('Que rico es la bandeja paisa')


# En base al número del dia de la semana si es 1 es lunes, si es 2 es martes, si es 3 es miíercoles y asi sucesivamente

numero = 1
dia = ""
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miércoles"
#...


# Crear una calculadora simple en la cual vamos a ingresar el numero1, operación que puede ser "+" (Suma), "-" (Resta), "*" (multiplicación), "/" (división), numero2, retornar el resultado

numero1 = int(input("Ingresa el primer número: "))
operador = input("Ingresa el operador: ")
numero2 = int(input("Ingresa el segundo número: "))

if operador == "+":
    print(f'El resultado de la suma es: {numero1 + numero2}')
elif operador == "-":
    print(f'El resultado de la suma es: {numero1 - numero2}')
elif operador == "*":
    print(f'El resultado de la suma es: {numero1 * numero2}')
elif operador == "/":
    print(f'El resultado de la suma es: {numero1 / numero2}')
else:
    print("Operador no válido")


# Otra forma de resolver el ejercicio:
n1 = int(input("Ingresa el primer número: "))
op = input("Ingresa el operador: ")
n2 = int(input("Ingresa el segundo número: "))
resultado = ''

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 == 0:
        resultado = "No se puede dividir entre 0"
    else:
        resultado = n1 / n2
else:
    resultado = "INCORRECTO"

print(resultado)