# EJERCICIO 1
# Solicita por teclado un numero que representa una cantidad total de segundos.
# Calcula cuantas horas, minutos y segundos representa (usando los operadores // y %) e imprime el resultado con un f-string. Ejemplo: "3746 segundos equivalen a 1 horas, 2 minutos y 26 segundos".

total_segundos = int(input("Ingresa la cantidad total de segundos: "))

horas = total_segundos // 3600
min = (total_segundos % 3600) // 60
seg = total_segundos % 60

print(f"{total_segundos} segundos equivalen a {horas} horas, {min} minutos y {seg} segundos.")