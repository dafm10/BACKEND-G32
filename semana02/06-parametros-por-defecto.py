# Si al crear una función le colocamos su valor al parámetro, entonces si al momento de llamar a la función no se le da ese parámetro, usaría el valor por defecto
def saludar(saludo="Buenas noches"):
    print(saludo)

saludar()
saludar("Hola")
saludar(saludo="Aloha")

# NOTA: Si queremos utilizar parámetro y parámetros con valor predeterminado, los parámetros con valores predeterminados van al final
def registrar_alumno(nombre, curso="Backend"):
    print(f"El alumno {nombre} fue registrado al curso de {curso}")

registrar_alumno("Eduardo")
registrar_alumno("Martita", "Frontend")

# 1. Crear una función calcular_dscto en la cual tendremos el parámetro de precio y procentaje, si no se da el porcentaje su valor debe ser 10, calcular el descuento de 3 productos, en los cuales dos de ellos no se les pase el parámetro de porcentaje

def calcular_dscto(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    monto = precio - descuento
    print(f"El precio {precio} su descuento es {descuento} y el monto final sería {monto}")

articulos = [{"monto": 500}, {"monto": 1200}, {"monto": 80, "tasa": 25}]
for articulo in articulos:
    # calcular_dscto(articulo.get("monto"), articulo.get("tasa")) if articulo.get("tasa") else calcular_dscto (articulo.get("monto"))
    if articulo.get("tasa"):
        calcular_dscto(articulo.get("monto"), articulo.get("tasa"))
    else:
        calcular_dscto(articulo.get("monto"))

# calcular_dscto(20)
# calcular_dscto(50)
# calcular_dscto(75, 25)

