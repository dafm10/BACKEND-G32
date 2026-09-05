class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_info(self):
        print(f"{self.nombre} gana {self.sueldo}")


# Heredo mi clase
class EmpleadoVentas(Empleado):
    pass


# Al heredar de una clase jalaremos toda su configuración (métodos y atributos públicos y protegidos)
vendedor = EmpleadoVentas("Roxana", 2000)
vendedor.mostrar_info()

# Clase padre / superclase > La clase original (Empleado)
# Clas ehija / subclase > La clase que hereda (EmpleadoVentas)
# Herencia > La hija obtiene automáticamente atributos y métodos del padre


class EmpleadoMkt(Empleado):
    def __init__(self, nombre, sueldo, comision):
        # cuando quremos reutilizar el mismo método de clase padre usamos super()
        super().__init__(nombre, sueldo)
        self.comision = comision


##################################################


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo :P")

    def dormir(self):
        print(f"{self.nombre} está durmiendo zzz")


class Gato(Animal):
    # si queremos sobre-escribir algún método del padre
    def __init__(self, nombre, edad):
        self.edad = edad
        super().__init__(nombre)

    def araniar(self):
        print(f"{self.nombre} está arañando")

    def dormir(self):
        # Si no mandamos a llamar al método del padre (super()) estaremos SOBREESCRIBIENDO el comportamiento del método en el hijo
        print(f"{self.nombre} está en el techo durmiendo sabroso")


class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def comer(self):
        super().comer()
        print(f"Está comiendo feliz!")


g = Gato("Michi", "15 meses")
p = Perro("Chiwi")
g.comer()
g.araniar()
p.dormir()
p.ladrar()
p.comer()


# 1. Crear una clase padre llamada Figura y dos clases hijos llamada Cuadrado y Triángulo. La clase Figura tiene el atributo nombre y un método área() que retorna 0 por defecto. La clase Cuadrado tiene un atributo adicional que es lado y la clase Triángulo tiene atributo base y altura, ambas clases heredan de Figura y se necesita sobreescribir el método area()


class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def area():
        return 0


class Cuadrado(Figura):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.lado = lado

    def area(self):
        return self.lado**2


class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


c = Cuadrado("Cuadrado", 5)
print(c.area())

t = Triangulo("Triangulo", 12, 4)
print(t.area())


# 2. Clase Persona y clase Guerrera y Mago, en la cual Persona tiene nombre y vida (valor predeterminaro es 100) y un método recibir_danio(cantidad) que resta vida hasta llegar a 0. Guerrero tiene el atributo fuerza y un método atacar() que imprime el daño causado según la fuerza que tenga. La clase Mago tiene atributo maná y un método lanza_hechizo() que solo funciona si tiene suficiente maná (si no muestra un mensaje de error)


class Persona:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, cantidad):
        if self.vida - cantidad < 0:
            return "Ya se murió"

        self.vida -= cantidad


class Guerrero(Persona):
    def __init__(self, nombre, fuerza, vida=100):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self):
        return f"Has hecho {self.fuerza} puntos de daño"


class Mago(Persona):
    def __init__(self, nombre, mana, vida=100):
        super().__init__(nombre, vida)
        self.mana = mana

    def lanza_hechizo(self, costo_de_mana):
        if costo_de_mana > self.mana:
            return "No se puede lanzar el hechizo por falta de maná!"

        return "Lanzando el hechizo"


persona = Persona("Anakin", 80)
print(persona.recibir_danio(110))

persa = Guerrero("Leonidas", 100)
print(persa.atacar())

merlin = Mago("Merlin", 50, 70)
merlin.recibir_danio(20)
print(merlin.lanza_hechizo(100))
print(merlin.lanza_hechizo(40))
