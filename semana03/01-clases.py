# CLASE: Bloque de código que permite crear código que luego se podrá reutilizar

# Persona
# ojos, orejas, brazos, cabello, dientes (ATRIBUTOS)
# caminar, correr, nadar, lanzar (MÉTODOS)
# toda CLASE tiene atributos y métodos

class Persona:
    nombre = ""
    edad = 0

# Instanciar > Crear una copia completa de toda la clase
# al momento de crear una instancia TODOS LOS ATRIBUTOS Y MÉTODOS van a ser PROPIOS de esa variable
p1 = Persona()
p2 = Persona()
print(type(p1))

# Para acceder a los ATRIBUTOS de clase?
p1.nombre = "Eduardo"
p2.nombre = "Ana"

# Al editar un atributo de la instancia solamente se va a modificar en esa instancia y no en las otras
print(p1.nombre)
print(p2.nombre)

# Si al momento de crear un statement (bloque de código) y este no tenemos lista la lógica, se le pone "pass" para que no me de errores de identación y dejar la lógica para más tarde.

# Si una clase al momento de crear su instancia quiero inicializar los atributos, entonces debemos usar el constructor

class Gato:
    # Cuando creamos una función dentro de una clase, esta pasa a llamarse método (por que solo va a funcionar dentro de la clase)
    # en python SIEMPRE el primer parámetro de un método es "self (así mismo), sirve para indicar que los cambios que hagamos se realicen a la misma instancia de la Clase"
    # en python no hay this, se usa self

    # si creo un atributo, pero ese no lo pongo dentro del inicializador, este atributo no se configurará cuando cree la instancia pero igual se puede acceder a el
    def __init__(self, nombre, raza, peso):
        # para usar cualquier atributo o método de la misma clase, usamos el "SELF"
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        # las variables que yo cree dentro de __init__ estos serán creados como atributos de la clase y podrán ser usados en todos su métodos

g1 = Gato("Michi", "Persa", 2.5)