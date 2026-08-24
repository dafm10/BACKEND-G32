# Colección de datos Editable pero no es ordenada
# Se suelen utilizar para almacenar información y luego corroborar su contenido sin importar algún orden en específico

roles = {"USUARIO", "ADMIN", "INVITADO", "ALUMNO", "PROFESOR"}

# No es posible acceder a un conjunto por su posición
# print(roles[1])


# Asi se agrega nuevos datos a mi conjunto
roles.add("SUPERADMIN")

# Asi se elimina los datos del conjunto
roles.remove("USUARIO")
roles.add("SUPERADMIN")
print(roles)

# Los conjuntos (SET) se usan para poder evitar duplicidad de información, es decir, si se intenta agregar el mismo valor de una vez lo omitirá, esto es sensible a Mayus y Minus

# not in > no está
# in > está
# is > es / ser
print("COORDINADOR" in roles)
print("ALUMNO" in roles)
