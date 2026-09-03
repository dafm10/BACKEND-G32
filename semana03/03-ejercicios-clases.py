# 1. Crear una clase Producto en el cual su constructor reciba el nombre, precio, stock. Agregar un método está_disponible en el cual muestre True si lo está o no.

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def esta_disponible(self):
        if self.stock > 0:
            return "Está disponible"
        else:
            return "Producto sin stock"

p1 = Producto("Atún", 3.5, 5)
p2 = Producto("Aceite", 8.5, 0)

print(p1.esta_disponible())
print(p2.esta_disponible())


# 2. Crear una clase CarritoCompras en la cual en el constructor reciba el cliente y que inicialice una lista vacía de productos. Así mismo tener los métodos agregar_producto(nombre, precio), y cada producto se debe de guardar en un diccionario {"nombre": nombre, "precio":precio} a la lista. Y otro método llamado calcular_total en el cual recorrerá la lista de productos y me dará el precio a pagar. Y un método llamado limpiar_carrito en el cual limpiará todos los productos de la lista.

class CarritoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += float(producto["precio"])
        return f"El total a pagar es: S/. {total}"

    def limpiar_carrito(self):
        self.productos.clear()

car = CarritoCompras("David")
car.agregar_producto("Leche", 15)
car.agregar_producto("Arroz", 22.5)
car.agregar_producto("Cereal", 11.2)
car.agregar_producto("Yogurt", 19.9)
print(car.productos)
print(car.calcular_total())
car.limpiar_carrito()
print(car.productos)

# 3. Crear una clase llamada Sesion (simular el login y logout) en la cual en el constructor recibamos un usuario y un atributo que sea activa = False. Agregar el método iniciar_sesion que cambia activa = True y cerrar_sesion que cambia activa = False y un método verificar_acceso que imprima "Acceso Permitido" si activa = True o "Acceso denegado" si activa = False


class Sesion:
    def __init__(self, usuario, active = False):
        self.usuario = usuario
        self.active = active

    def iniciar_sesion(self):
        self.active = True
        
    def verificar_acceso(self):
        resultado = "Acceso Permitido" if self.active else "Acceso Denegado"
        print(resultado)

    def cerrar_sesion(self):
        self.active = False

sesion = Sesion("dave")
sesion.iniciar_sesion()
print(sesion.verificar_acceso())
sesion.cerrar_sesion()
print(sesion.verificar_acceso())