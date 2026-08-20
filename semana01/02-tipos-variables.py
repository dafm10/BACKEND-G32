# String (texto)
# se identifican por tener comilla simple o doble
# se puede crear strings pero de varias lineas, usando la triple doble comilla
nombre = 'David O\'Conner'
nombre = "Davod O'Conner"

#al poner el carácter 'r' al comienzo del string este interpretará el uso del back-slash como un caracter más y no para poder hacer uso de caracteres especiales
ruta = r'C:\documents\etc'
print(ruta)
texto = '''Hola, ya estamos en clase
El dia de hoy continuaremos avanzando con Python.
        Hoy haremos varios ejercicios'''

apellido = "De Rivero"

persona = 'David'
# el prefijo 'f' hace que lo que ponga entre {} podrá ser código python
saludo = f'Hola {persona}, mucho gusto'
print(saludo)
# si no quieres usar el prefijo 'f'
# para el uso del método format, la misma cantidad de llaves debe ser igual a la cantidad de parámetros
saludo = 'Hola {}, mucho gusto'.format(persona)
print(saludo)

# Enteros o Int
edad = 30

# Decimales ó Float
estatura = 1.88

# Boolean
aprobado = True
repite = False

# las variables en python nunca pueden comenzar con números, tampoco con caracteres especiales.
# no se recomienda comenzar con _ porque puede malentenderse con encapsulamento de POO

# Para saber el tipo de variable se usa la función 'type'
print(type(edad))