# En Python también se pueden pasar N parámetros con el nombre del parámetro usando los **kwargs (keyword arguments)
def crear_perfil(id, **datos):
    # el kwargs se almacena en formato de un diccionario
    # Se necesita enviar un correo de bienvenida si a la función se le pasa el parámetro correo ó email
    if datos.get("correo") or datos.get("email"):
        print("Se envió el correo de bienvenida")
    else:
        print("No se envió el correo")

    print(id)
    print(datos)

crear_perfil(id="1", nombre="Eduardo", edad=30)
crear_perfil(id="2", nombre="Valeria", nacionalidad="Peruana", estado_civil="Viuda", email="val123@hotmail.com")


# Se puede combinar los *args con los **kwargs, pero siguiendo el orden de primero los args y los kwargs
def registrar_alumno(nombre, *cursos, **datos_extra):
    print(f"Alumno {nombre}")
    print("Cursos inscritos:")
    for curso in cursos:
        print(f"* {curso}")
    print("Datos adicionales:")
    for clave, valor in datos_extra.items():
        print(f"* {clave}: {valor}")

registrar_alumno("David", "Python", "Flask", "Djando", edad= 30, ciudad="Arequipa", hobbies=["Nadar", "Enseñar", "Jugar"])



# Crear una función calcular_total que reciba cualquier cantidad de montos (números) y un parámetro con el nombre moneda (kwargs) con el valor de la divisa, por defecto será USD si no se envía nada.

def calcular_total(*montos, **otros_valores):
    total = 0
    for monto in montos:
        total += monto
    # .get como segundo parámetro se le puede pasar un valor por defecto
    divisa = otros_valores.get("moneda", "USD")
    print(f"Total: {total}{divisa}")

calcular_total(100, 250, 500, moneda="PEN")
calcular_total(200, 500, 1000)