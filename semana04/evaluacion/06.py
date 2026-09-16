# EJERCICIO 6
# Crea un programa que simule un cajero automatico simple usando un bucle while:

# * La clave correcta es "2024".
# * El usuario tiene un maximo de 3 intentos.
# * Si acierta, debe mostrar "Acceso concedido" y terminar el bucle (usa break).
# * Si falla los 3 intentos, debe mostrar "Cuenta bloqueada".
# * Usa try-except para capturar el caso en que el usuario ingrese texto en lugar de numeros, si tu programa espera un numero en algun momento (opcional, pero valorado como plus).

def cajero_automatico():
    clave_correcta = 2024
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        try:
            clave = int(input("Ingresa tu clave: "))
            if clave == clave_correcta:
                print("Acceso concedido")
                break
            else:
                intentos += 1
                print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos")
        except ValueError:
            print("La clave debe ser un número")
            intentos += 1
    else:
        print("Cuenta bloqueada por exceder el número de intentos")

cajero_automatico()