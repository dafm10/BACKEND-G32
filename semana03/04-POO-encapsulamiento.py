class CuentaBancaria:
    def __init__(self, titular, saldo, cuenta):
        self.titular = titular
        self.saldo = saldo
        # atributo protegido se crea con un subguión, no se puede acceder fuera de la clase
        # Python es muy permisivo con los atributos protegidos, es decir, si me va a permitir acceder al atributo fuera de la clase pero es por una CONVENCION (buenas practicas) que no debo acceder a el fuera de la clase. Cosa que si se cumple en otros lenguajes de programación como Java, C++, C#, entre otros
        # Si se pueden heredar
        self._cuenta = cuenta
        # Cuando el atributo empieza con doble subguión este es PRIVADO, este atributo no se poderá acceder
        # No se puede heredar hacia otras clases hijas
        self.__entidad_financiera = "BCP"

cuenta1 = CuentaBancaria("Eduardo", 500, "100-1323443434-201")
print(cuenta1.saldo)
# Se puede modificar los atributos que son PUBLICOS
cuenta1.saldo = 2500
print(cuenta1.saldo)
print(cuenta1._cuenta)
# print(cuenta1.__entidad_financiera) # AttributeError > error cuando el atributo no existe


# Para exponer atributos privados/protegidos de forma controlada se suele utilizar el decorador @property en vez de getters y setters como en Java
# getter | setter > son métodos que sirven para devolver (getter) y modificar (setter) el valor del atributo protegido o privado

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__apellido = "Xi"

    # Luego del decorador siempre se llama a un método por que el decorador modifica la función adyacente con la propiedad del decorador, en este caso, el decorador property sirve para definir la devolución del contenido del atributo privado
    @property
    def nombre(self):
        return self.__nombre

    # Asi mismo se puede utilizar los métodos para modificar y eliminar el contenido del atributo privado
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido


p1 = Persona("Eduardo")
print(p1.nombre)
p1.nombre = "Dave"
print(p1.nombre)
print(p1.apellido)



# Crear una clase Usuario en el cual tengamos el nombre, correo, password. El password debe ser un atributo privado y solamente en el constructor inicializar el nombre y correo. Cuando se quiera modificar el password usar el @property y no permitir el ingreso de un string que tenga espacios o sea menor que 8 caracteres, y así mismo cuando se quiera obtener el password devolver *********

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.__password = None

    @property
    def password(self):
        return "******" if self.__password else "Ingrese un password"

    @password.setter
    def password(self, nuevo_password):
        if " " in nuevo_password or len(nuevo_password) < 8:
            print("Password inválida, no puede tener espacios ni ser menor a 8 caracteres")
        self.__password = nuevo_password

usuario1 = Usuario("Pedro", "peter@gmail.com")
print(usuario1.password)
usuario1.password = "dave"
usuario1.password = "dave2026"
print(usuario1.password)



class Empleado:
    def __init__(self, nombre, sueldo_base, horas_extras):
        self.nombre = nombre
        self.__sueldo_base = sueldo_base
        self.__horas_extras = horas_extras

    def __calcular_pago_extra(self):
        valor_hora_extra = 20
        return self.__horas_extras * valor_hora_extra

    def calcular_sueldo_total(self):
        monto_extra = self.__calcular_pago_extra()
        return self.__sueldo_base + monto_extra

    def mostrar_boleta(self):
        print(f"""Empleado: {self.nombre}
Sueldo base: {self.__sueldo_base}
Pago extra: {self.__calcular_pago_extra()}
Total: {self.calcular_sueldo_total()} """)

emp1 = Empleado("Juanito", 2000, 15)
# emo1.__calcular_pago_extra() # No se puede acceder a los métodos privados
emp1.mostrar_boleta()



# Crear una clase Caja que simule una caja registradora
# Un atributo privado __total que inicia en 0, y un método privado __validar_monto(monto) que retorne True si el monto es mayor que 0 y False si no lo es. Asi mismo otro método agregar_venta(monto) que primero valide el monto y si es válido lo incremente a total y muestre un mensaje de confirmación, si no es válido, mostrar un mensaje de rror y no modificar el total. Y un método mostrar_total() que imprima lo acumulado en caja.

class Caja:
    # Si el constructor no tiene parámetros, los atributos se pueden definir en la raiz de la clase
    __total = 0

    # def __init__(self):
    #     self.__total = 0

    def __validar_monto(self, monto):
        return monto > 0

    def agregar_venta(self, monto):
        es_valido = self.__validar_monto(monto)
        if es_valido:
            self.__total += monto
            print("Monto agregado")
        else:
            print("Error el ingresar monto negativo")

    def mostrar_total(self):
        print(f"En caja hay {self.__total}")


venta = Caja()
venta.agregar_venta(100)
venta.agregar_venta(20)
venta.agregar_venta(-5)
venta.mostrar_total()