# Ejercicio 1

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__sueldo_base = None

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo_base):
        if nuevo_sueldo_base < 0:
            print(f"Error: No puede tener sueldo base negativo")
            return

        self.__sueldo_base = nuevo_sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Sueldo: {self.calcular_sueldo()}")


class EmpleadoVentas(Empleado):
    def __init__(self, nombre, comision):
        super().__init__(nombre)
        self.comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision

class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.pago_por_hora

empleados = [Empleado("Eduardo"), EmpleadoVentas("Anita", 300), EmpleadoTiempoParcial("Roxana", 80, 20)]

planilla = 0
for empleado in empleados:
    empleado.sueldo_base = 1500
    empleado.mostrar_info()

    planilla += empleado.calcular_sueldo()

print(f"TOTAL DE LA PLANILLA: {planilla:.2f}")


# Ejercicio 2

class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.__precio = None
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print(f"Error: El precio no puede ser negativo")
            return

        self.__precio = nuevo_precio

    def calcular_precio_final(self):
        return self.__precio

    def vender(self, cantidad):
        if cantidad <= self.stock:
            print(f"Venta Exitosa")
        else:
            print(f"Error: La venta no puede ser por que no hay stock del producto")


class ProductoConDescuento(Producto):
    def __init__(self, nombre, stock, porcentaje_descuento):
        super().__init__(nombre, stock)
        self.porcentaje_descuento = porcentaje_descuento

    def calcular_precio_final(self):
        descuento = self.precio * (self.porcentaje_descuento / 100)
        return self.precio - descuento


class ProductoImportado(Producto):
    def __init__(self, nombre, stock, impuesto_aduanero):
        super().__init__(nombre, stock)
        self.impuesto_aduanero = impuesto_aduanero

    def calcular_precio_final(self):
        impuesto = self.precio * (self.impuesto_aduanero / 100)
        return self.precio + impuesto


productos = [Producto("Cuaderno", 5), ProductoConDescuento("Mochila", 20, 15), ProductoImportado("Laptop", 300, 18)]

for producto in productos:
    producto.precio = 500

productos[0].vender(10) # Imprimir venta inválida
productos[1].vender(5) # Venta válida
productos[2].vender(1) # Venta válida