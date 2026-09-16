# EJERCICIO 7

# Se necesita construir un pequeño sistema para gestionar el pago de distintos tipos de empleados de una empresa.

# REQUERIMIENTOS:

# 1. (1.5 puntos) Crea una clase base llamada Empleado con:
# * Atributos: nombre (publico) y sueldo_base (debe ser un atributo PRIVADO, es decir, con doble guion bajo).
# * Un getter y un setter para sueldo_base usando el decorador @property. El setter NO debe permitir que se asigne un sueldo_base negativo (si se intenta, mostrar un mensaje de error y no modificar el valor).
# * Un metodo calcular_sueldo() que por defecto retorne el sueldo_base.
# * Un metodo mostrar_info() que imprima el nombre y el resultado de calcular_sueldo().

# 2. (1.5 puntos) Crea una clase EmpleadoVentas que herede de Empleado y agregue un atributo comision. Debe sobreescribir el metodo calcular_sueldo() para que retorne sueldo_base + comision. Usa super() en el constructor.
# 3. (1.5 puntos) Crea una clase EmpleadoTiempoParcial que herede de Empleado y tenga los atributos horas_trabajadas y pago_por_hora. Debe sobreescribir calcular_sueldo() para que retorne horas_trabajadas * pago_por_hora (en este caso se ignora el sueldo_base). Usa super() en el constructor.
# 4. (0.5 puntos) Crea una lista con al menos un objeto de cada una de las 3 clases (Empleado, EmpleadoVentas y EmpleadoTiempoParcial). Recorre la lista con un for llamando a mostrar_info() en cada uno (esto demuestra el POLIMORFISMO, ya que cada clase calcula su sueldo de forma distinta con el mismo nombre de metodo).
# 5. (Sin puntaje adicional, pero obligatorio) Al final del for, suma el resultado de calcular_sueldo() de cada empleado en una variable llamada planilla_total e imprime el total con 2 decimales.


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo):
        if sueldo < 0:
            print("El sueldo no debe ser menor a 0")
            self.sueldo_base = 0
        else:
            self.__sueldo_base = sueldo

    def calcular_sueldo(self):
        return self.sueldo_base

    def mostrar_info(self):
        print(f"{self.nombre}, tu sueldo calculado es: S/. {self.calcular_sueldo():.2f}")


class EmpleadoVentas(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision


class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_x_hora):
        super().__init__(nombre, 0)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_x_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora


empleado1 = Empleado("Pedro", 2000)
empleado2 = EmpleadoVentas("Abril", 1500, 400)
empleado3 = EmpleadoTiempoParcial("Dave", 55, 15)

empleados = [empleado1, empleado2, empleado3]

planilla_total = 0

for empleado in empleados:
    empleado.mostrar_info()
    planilla_total += empleado.calcular_sueldo()
    print("************************")

print("************************")
print(f"El pago total de la planilla es: S/. {planilla_total:.2f}")