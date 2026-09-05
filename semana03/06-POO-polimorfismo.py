# Polimorfismo > Poli (muchos) | morfo (formas) > muchas formas de poder tener el mismo método pero con diferente resultado, esto va a depender de la clase donde se encuentre
class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        # Si queremos reutilizar el contenido del método padre lo llamamos usando super()
        super().hacer_sonido()
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")

# lista de instancias
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    # el mismo método tiene diferente resultado (forma)
    animal.hacer_sonido()

# El polimorfismo sirve para escribir código más genérico indicando que siempre voy a tener ese método por que está "dentro de la familia" y no voy a tener que validar que el método existe antes de llamarlo, sea cual sea la clase
# Es la base de muchos patrones de diseño y de las librerias como Django, Flask