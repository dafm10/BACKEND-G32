nombre = input('Ingresa tu nombre: ')

print(f'Tu nombre es {nombre}')

# todo lo que se ingresa por el input SIEMPRE es String
# en Python para convertir un tipo de dato a otro, solo se necesita invocar al tipo de dato que queremos usar
edad = '34'
# Así se convierte a un entero (int)
edad_numerica = int(edad)
# NOTA: No se puede convertir cualquier cosa, hay que tener coherencia.
# edad_numerica = int('Treinta y cuatro')