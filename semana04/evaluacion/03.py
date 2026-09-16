# EJERCICIO 3
# Dado el siguiente diccionario:

curso = {
    "nombre": "Backend con Python",
    "duracion_semanas": 12,
    "estudiantes": ["Ana", "Luis", "Carla", "Pedro"],
    "profesor": {
        "nombre": "Eduardo",
        "ciudad": "Arequipa"
    }
}

# Escribe el codigo necesario para imprimir:
# a) El nombre del curso.
# b) El segundo estudiante de la lista (posicion 1).
# c) La ciudad del profesor.
# d) La cantidad total de estudiantes (usando len()).

print(f"El nombre del curso es: {curso['nombre']}")
print(f"El segundo estudiante de la lista es: {curso['estudiantes'][1]}")
print(f"El profesor es de la ciudad de: {curso['profesor']["ciudad"]}")
print(f"El curso tiene un total de: {len(curso['estudiantes'])} estudiantes")