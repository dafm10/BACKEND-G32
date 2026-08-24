# es una Colección de datos ordenada POR LLAVES y EDITABLE
# las llaves siempre tienen que ser tipo STRING

alumno = {
    # llave : valor
    "nombre": "Juan",
    "apellido": "Zegarra",
    "curso": "Python",
    "hobbies": ["nadar", "programar", "trabajar"],
    "edad": 35,
    "jubilado": False,
    "padres": {
        "padre": {
            "nombre": "Alberto",
            "apellido": "Zegarra"
        },
        "madre": {
            "nombre": "Lucía",
            "apellido": "Hinojosa"
        }
    }
}

print(alumno["nombre"])
# Si quiero acceder de forma segura a una de mis llaves
# si no existe esa llave retornará None (vacío) o el valor que le pongamos como segundo parámetro
# el método GET sirve para obtener las propiedades o llaves del diccionario
print(alumno.get("nombres", "No existe")) # retorma em pantalla: NO EXISTE

# retorna todas las llaves del diccionario
print(alumno.keys())

# retorna todos los valores del diccionario
print(alumno.values())

# para hacer asignaciones SI o SI usamos los corchetes y no el método GET, ese solo es para obtener información
alumno['nacionalidad'] = 'Peruano'
print(alumno["nacionalidad"])