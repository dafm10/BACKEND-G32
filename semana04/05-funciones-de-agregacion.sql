-- FUNCIONES DE AGREGACIÓN | AGGREGATE FUNCTIONS
-- sirve para poder tener un poco de lógica en nuestras consultas

-- GROUP BY > se usa está claúsua para agrupar
-- Al usar GROUP BY se tiene que agrupar todas las columnas que se seleccionan
SELECT categoria FROM productos
-- WHERE
GROUP BY categoria;

-- https://www.postgresql.org/docs/9.5/functions-aggregate.html

-- COUNT > Contar
SELECT activo, COUNT(activo) FROM productos GROUP BY activo;

-- SUM > Sumar
-- Visualizar los stock de los productos activos e inactivos
SELECT activo, SUM(stock) FROM productos GROUP BY activo;

SELECT categoria, SUM(stock) AS suma FROM productos WHERE activo = true GROUP BY categoria;


-- AVG > Promedio
-- El promedio de los precios por categoría.
SELECT categoria, AVG(precio) AS promedio FROM productos GROUP BY categoria;


-- MIN / MAX > Devuelve los valores mínimos ó máximos
-- Mostrar los valores máximos de los precios por categoría, pero que solo sean activos.
SELECT categoria, MAX(precio) FROM productos WHERE activo = TRUE GROUP BY categoria;


-- Si queremos usar una funciín de agregación para condicionales, entonces usamos la clausula HAVING.
SELECT categoria, SUM(stock) AS suma FROM productos WHERE activo = true GROUP BY categoria HAVING SUM(stock) >= 40 ORDER BY SUM(stock) DESC, categoria DESC;