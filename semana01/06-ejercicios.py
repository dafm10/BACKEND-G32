# 1. Ingresar por teclado el monto a pagar y que me imprima por consola el monto de propina que debo de dar siendo el 10%

montoPago = int(input('Ingresa el monto a pagar: '))
propina = montoPago * 0.10
print(f'El monto de propina es: {propina}')


# 2. Dado un total de segundos (3746), calcula cuantas horas, minutos y segundos representan, usando los operadores aritmeticos // y %

totalSeg = 3746
horas = totalSeg // 3600
segundosRest = totalSeg % 3600

min = segundosRest // 60
seg = segundosRest % 60

print(f'{horas} horas, {min} minutos y {seg} segundos')


# otra forma
segundos = 3746
horas = segundos // 3600 # // es por que queremos la parte entera
minutos = (segundos - (horas * 3600)) // 60 # 1 hora : 60 minutos
totalSegundos = segundos - (minutos * 60 + horas * 3600)

print(f'{segundos} segundos es {horas} hora con {minutos} minutos y {totalSegundos} segundos')

# 1h con 2 minutos y 26 segundos



# 3. Ingresa un número y quiero que me diga si es PAR ó IMPAR (use el oprtador airmético %)

num = int(input('Ingresa un número y te diré si par o impar: '))
# if (num % 2) == 0:
#     print(f'El número {num}, es PAR')
# else:
#     print(f'El número {num}, es IMPAR')

resultado = num % 2
print(f'El numero es {resultado}')

# 4. Ingresa un monto por teclado y luego haga lo siguiente: 1. aumente 250, luego retire 400 y luego genere un cobro de interés del 5% (multiplicar por 1.05)

monto = float(input('Ingresa un importe: '))
monto += 250
monto -= 400
monto *= 1.05
print(f'El importe descontando el interes es de: {monto}')
