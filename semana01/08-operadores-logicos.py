# Sirve para comparar varios operadores de comparación

tiene_dinero = True
tiene_tiempo = True
tiene_energia = False

# and > todas las condiciones tienen que ser verdaderas, si alguna es false, todo es falso
print(tiene_dinero and tiene_tiempo and tiene_energia)

# or > basta con que una condición sea verdadera, para que todo sea TRUE
print(tiene_dinero or tiene_tiempo or tiene_energia)