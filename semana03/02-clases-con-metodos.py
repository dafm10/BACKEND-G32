class Mueble:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def dimensiones(self):
        print(f"""Las dimensiones son:
        Largo: {self.largo}
        Ancho: {self.ancho} 
        Alto: {self.alto}""")


m1 = Mueble(1.4, 0.7, 1.2)
m1.dimensiones()
# si se quiere cambiar los valores ingresados al inicio
m1.largo = 1.8
m1.dimensiones()

# Si no se le pasa el self como primer parámetro, ese método solo podrá ser accedido directo desde la clase, es decir, sin instancia
# Mueble.dimensiones()

# EJERCICIO
# 1. Crear una clase Rectangulo en la cual tengamos en el constructor la base y la altura y tener un método para calcular su área calcular_area en la cual retorn el área (base x altura)

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print(f"El área del rectángulo es: {self.base * self.altura}")

r1 = Rectangulo(10, 5)
r1.calcular_area()


# 2. Crear una clase estudiante en la cual tenga el atributo nombre, notas, correo, que deben ser inicializados el nombre y el correo y tenga su método agregar_nota(nota), también su método promedio() que me de el promedio de todas las notas y el método estado que me de su estado si está Aprobado (>=13), Subsa (11 - 12) ó Jalado (0 - 10)
# Se puede utilizar una llamada a un método dentro de otro (algo así como llamar a una función dentro de otra)

class Estudiante:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        total = 0
        for nota in self.notas:
            total += nota
        promedio = total / len(self.notas)

        return promedio

    def estado(self):
        promedio = self.promedio()

        if promedio >= 13:
            return "Aprobado"
        elif 10 <= promedio < 13:
            return "Subsa"
        elif 0 <= promedio < 10:
            return "Jalado"

estudiante1 = Estudiante("Eduardo", "erivero@gmail.com")
estudiante1.agregar_nota(10)
estudiante1.agregar_nota(15)
estudiante1.agregar_nota(18)

estudiante2 = Estudiante("Julia", "jnunez@gmail.com")
estudiante2.agregar_nota(18)
estudiante2.agregar_nota(5)
estudiante2.agregar_nota(10)

print(estudiante1.estado())
print(estudiante2.estado())