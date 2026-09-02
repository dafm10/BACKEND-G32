# en python tenemos la posibilidad de crear funciones de una sola línea y estas se conocen como funciones lambda
# automáticamente retorna el resultado de la operación
sumar = lambda num1, num2: num1 + num2 if num1 > 10 else num1 * num2

# Todo esto se resume usando lambda
# def sumar(num1, num2):
#     if num1 > 10:
#         return num1 + num2
#     else:
#         return num1 * num2

resultado = sumar(10, 20)
print(resultado)


# 1. Necesito una función es_correo que verifique que el correo contiene un "@" y un "." usando lambda functions y además dentro de los str se puede usar la palabara "in" para ver si está o no está ese caracter.

es_correo = lambda correo: "@" in correo and "." in correo
print(es_correo("dafmgmail.com"))
print(es_correo("dafm@gmailcom"))
print(es_correo("dafm@gmail.com"))

# 2. Necesito una función generar_slug
# slug es convertir el texto "Bienvenidos a la clase" a "bienvenidos-a-la-clase", es decir, convierte los espacios por guiones y lo pone todo en minúscula
# pueden usar la función .lower() y la función .replace()
generar_slug = lambda texto : texto.lower().replace(" ", "-") # esto se llama anidamiento de métodos

print(generar_slug("Bivenidos a la Clase"))