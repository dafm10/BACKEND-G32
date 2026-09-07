# 1. Crear un sistema para calcular sueldos de distintos tipos de empleados
# Clase base Empleado
# atributos: nombre (publico) y sueldo_base (privado)
# crear su getter y setter para el sueldo_base (el setter no debe permitir valores negativos)
# metodo calcular_sueldo() que retorna el sueldo_base
# mostrar_info() imprime el nombre y el sueldo calculado

# Clase hijas
# EmpleadoVentas y su atributo comision (monto fijo) y sobreescribir calcular_sueldo() para que retorne el sueldo_base + comision
# EmpleadoTiempoParcial y sus atributos horas_trabajadas y pago_por_hora y sobreescribir calcular_sueldo() para que retorne el horas_trabajas * pago_por_hora e ignora el sueldo base

# Para validar: 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Calcular e imprimir el total de la planilla (suma de todos los sueldos de los empleados)

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo):
        if sueldo < 0 :
            print("Ingresa un sueldo con rango positivo")
            self.sueldo_base = 0
        else:
            self.__sueldo_base = sueldo

    def calcular_sueldo(self):
        return self.sueldo_base

    def mostrar_info(self):
        print(f"{self.nombre}, tu sueldo es: S/. {self.calcular_sueldo():.2f}")

class EmpleadoVentas(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora

# Validando
empleado1 = Empleado("Juan", 2500)
empleado2 = EmpleadoVentas("Carlos", 2300, 500)
empleado3 = EmpleadoTiempoParcial("Dave", 1000, 75, 15)

empleados = [empleado1, empleado2, empleado3]

total_planilla = 0

for empleado in empleados:
    empleado.mostrar_info()
    total_planilla += empleado.calcular_sueldo()
    print("------------------------")

print(f"Total de la planilla: S/. {total_planilla:.2f}")



# --------------------------------------

# 2. Crear un sistema de inventario simple
# Clase base Producto
# atributos: nombre, precio(privado) y stock
# crear getter y setter para el precio (no negativos)
# metodo calcular_precio_final() que por defecto retorna el precio sin cambios
# metodo vender(cantidad) que resta del stock si hay suficiente, sino, muestra un mensaje de error y no resta stock

# Clases hijas
# ProductoConDescuento: atributo porcentaje_descuento. sobreescribir calcular_precio_final() aplicar el dscto sobre el precio
# ProductoImportado: atributo impuesto_aduanero (porcentaje). sobreescribir calcular_precio_final() para sumar ese impuesto al precio

# Para validar 
# 1. crear una lista con al menos un objeto de cada clase 
# 2. Recorrer la lista con un for llamando siempre al metodo mostrar_info() 
# 3. Intentar asignar un precio negativo a alguno de ellos usando el setter y comprobar el mensaje de error

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            print("El precio no puede ser menor a 0")
            self.__precio = 0
        else:
            self.__precio = precio

    def calcular_precio_final(self):
        return self.precio

    def vender(self, cantidad):
        if cantidad <= self.stock:
            print(f"Se vendió {cantidad} und. de {self.nombre}")
        else:
            print(f"Error: no hay suficiente stock de {self.nombre}, el stock actual es: {self.stock}")

    def mostrar_info(self):
        print(f"""
Producto: {self.nombre}, 
Precio base: S/. {self.precio}, 
Precio final: S/. {self.calcular_precio_final():.2f}
Stock: {self.stock}""")

class ProductoConDescuento(Producto):
    def __init__(self, nombre, precio, stock, porcentaje_dscto):
        super().__init__(nombre, precio, stock)
        self.porcentaje_dscto = porcentaje_dscto

    def calcular_precio_final(self):
        return self.precio - (self.precio * (self.porcentaje_dscto / 100))

class ProductoImportado(Producto):
    def __init__(self, nombre, precio, stock, impuesto_aduanero):
        super().__init__(nombre, precio, stock)
        self.impuesto_aduanero = impuesto_aduanero

    def calcular_precio_final(self):
            impuesto = self.impuesto_aduanero / 100
            return self.precio + (self.precio * impuesto)

producto1 = Producto("Mouse", 25, 5)
producto2 = ProductoConDescuento("Laptop", -3500, 10, 10)
producto3 = ProductoImportado("CPU", 800, 20, 26)

productos = [producto1, producto2, producto3]

for producto in productos:
    producto.mostrar_info()
    print("*************************")

producto1.vender(7)
producto2.vender(5)