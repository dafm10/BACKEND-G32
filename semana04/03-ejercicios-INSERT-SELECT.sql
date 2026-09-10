-- Crear una BD tienda
-- Ingresar a la BD tienda
-- Crear una tabla llamada productos cuyas columnas son
-- id autoincrementable pk
-- nombre texto no nullo
-- categoría texto hasta 40 caracteres
-- precio floeat con 2 decimales
-- stock entero
-- activo BOOLEAN DEFAULT TRUE

CREATE DATABASE tienda;
\c tienda
CREATE TABLE productos (
    id SERIAL PRIMARY KEY, 
    nombre TEXT NOT NULL, 
    categoria VARCHAR(40), 
    precio FLOAT(2), 
    stock INT, 
    activo BOOLEAN DEFAULT TRUE
);

-- Insertar los datos
INSERT INTO productos (nombre, categoria, precio, stock, activo)
VALUES
    ('Arroz Costeño 5kg', 'Abarrotes', 22.50, 40, TRUE),
    ('Fideos Don Vittorio', 'Abarrotes', 4.20, 0, TRUE),
    ('Coca Cola 1.5L', 'Bebidas', 6.50, 25, TRUE),
    ('Inca Kola 500ml', 'Bebidas', 3.00, 15, TRUE),
    ('Leche Gloria Evaporada', 'Lácteos', 4.80, 60, TRUE),
    ('Yogurt Gloria 1L', 'Lácteos', 8.90, 0, FALSE),
    ('Detergente Ariel 1kg', 'Limpieza', 15.90, 8, TRUE),
    ('Lejía Clorox 1L', 'Limpieza', 5.50, 30, TRUE),
    ('Atún Florida', 'Abarrotes', 6.90, 12, TRUE),
    ('Cerveza Cusqueña 620ml', 'Bebidas', 8.50, 0, FALSE);


-- CONSULTAS
-- 1. Mostrar todos los productos con todas su columnas
SELECT * FROM productos;

-- 2. Mostrar solo el nombre y precio
SELECT nombre, precio FROM productos;

-- 3. Mostrar nombre y precio pero cambia el nombre de la columna a nombre_producto y precio_soles
SELECT nombre AS nombre_producto, precio AS precio_soles FROM productos;

-- 4. Mostrar los productos cuya categoría sea 'Bebidas'
SELECT * FROM productos WHERE categoria = 'Bebidas';

-- 5. Mostrar los productos cuyo precio sea mayor a 10.00
SELECT * FROM productos WHERE precio_soles > 10;

-- 6. Mostrar los productos cuyo stock sea 0
SELECT * FROM productos WHERE stock = 0;

-- 7. Mostrar los productos cuyo precio sea entre 5 y 15 y cuyo nombre contenga la palabra Leche (sin sensible a mayúsculas)
SELECT * FROM productos WHERE precio_soles BETWEEN 5 AND 15 AND nombre_producto ILIKE '%Leche%';

-- 8. Mostrar los productos cuya categoría no sea 'limpieza'
SELECT * FROM productos WHERE categoria != 'Limpieza';
SELECT * FROM productos WHERE categoria <> 'Limpieza';

-- OPCIONAL
-- 9. Mostrar los productos que no estén activos
SELECT * FROM productos WHERE activo IS FALSE;
SELECT * FROM productos WHERE activo = FALSE;
SELECT * FROM productos WHERE activo = 'f';