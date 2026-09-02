try: # intentalo
    int(input("Inhresa un número: "))
except: # excepción (Si no lo intentó bien)
    print("Número inválido")

print("Yo aún sigo trabajando")



# También se puede filtrar los errores según su tipo
try: # intentalo
    numero = int(input("Inhresa un número: "))
    print(10 / numero)
# Generalmente se colocan los errores identificados
except ValueError:
    print("Número inválido")
except ZeroDivisionError:
    print("No se puede dividir entreo 0!")
# Y luego si por algún motivo se genera un nuevo error no registrado
except:
    print("Error desconocido!")