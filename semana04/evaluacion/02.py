# EJERCICIO 2
# Dada la siguiente lista de precios:

precios = [12.5, 8.9, 25.0, 3.75, 40.2]

# Usando un bucle for, calcula e imprime:
# a) La suma total de los precios.
# b) El promedio de los precios (con 2 decimales).

total_precios = 0
promedio = 0

for precio in precios:
    total_precios += precio

promedio = total_precios / len(precios)

print(f"La suma total es: S/. {total_precios}")
print(f"Promedio: S/. {promedio:.2f}")