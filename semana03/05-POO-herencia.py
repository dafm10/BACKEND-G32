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