-- EJERCICIO 8

-- Se necesita modelar una pequeña base de datos para una biblioteca.

-- EJERCICIO 8.1 - DDL (1.5 puntos)
-- Escribe las sentencias SQL necesarias para:
-- a) Crear una base de datos llamada biblioteca.

CREATE DATABASE biblioteca;
\c biblioteca

-- b) Crear una tabla llamada libros con las siguientes columnas:
-- * id: autoincrementable, llave primaria.
-- * titulo: texto, no nulo.
-- * autor: texto de hasta 50 caracteres.
-- * precio: numero decimal.
-- * stock: numero entero.
-- * disponible: booleano, con valor por defecto TRUE.

CREATE TABLE libros(
    id SERIAL PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor VARCHAR(50),
    precio NUMERIC(6,2),
    stock INT,
    disponible BOOLEAN DEFAULT TRUE
);

-- c) Crear una tabla llamada usuarios con:
-- * id: autoincrementable, llave primaria.
-- * nombre: texto.
-- * correo: texto, unico (UNIQUE).

CREATE TABLE usuarios(
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    correo TEXT UNIQUE
);

INSERT INTO usuarios (nombre, correo)
VALUES
('Dave', 'dave@gmail.com'),
('Pepe', 'pepito@gmail.com'),
('Luna', 'lunita@gmail.com'),
('Megan', 'megan@yagoo.es');

-- EJERCICIO 8.2 - DML e INSERT (1 punto)
-- Escribe las sentencias SQL para insertar al menos 4 registros (libros) en la tabla libros, variando sus categorias/valores de precio y stock (algunos con stock 0, otros con stock disponible).

INSERT INTO libros (titulo, autor, precio, stock, disponible)
VALUES
    ('Python a fondo', 'Oscar Ramirez Jiménez', 89.9, 10, TRUE),
    ('Python Cookbook', 'David Beazley', 99.50, 0, TRUE),
    ('Fluent Python', 'Luciano Ramalho', 49.9, 20, TRUE),
    ('Curso intensivo de Python', 'Oscar Ramirez Jiménez', 79, 16, FALSE);

INSERT INTO libros (titulo, autor, precio, stock, disponible)
VALUES
    ('POO', 'Oscar Ramirez Jiménez', 99.9, 8, TRUE),
    ('Desarrollo Web', 'David Beazley', 84.90, 0, TRUE),
    ('UX/UI', 'Luciano Ramalho', 69.9, 12, TRUE),
    ('Curso intensivo de JS', 'Oscar Ramirez Jiménez', 89.3, 10, FALSE),
    ('Diseño de interfaces', 'Oscar Ramirez Jiménez', 29.3, 4, TRUE);

-- EJERCICIO 8.3 - SELECT y filtros (1.5 puntos)
-- Utilizando la tabla libros del ejercicio anterior, escribe las consultas SQL para:
-- a) Mostrar todos los libros cuyo precio este entre 20 y 60.
SELECT * FROM libros WHERE precio BETWEEN 20 AND 60;
-- b) Mostrar todos los libros cuyo titulo contenga la palabra "Python" (sin distinguir mayusculas de minusculas).
SELECT * FROM libros WHERE titulo LIKE '%Python%';
-- c) Mostrar los libros que no tengan stock (stock = 0).
SELECT * FROM libros WHERE stock = 0;
-- d) Mostrar el titulo y autor de los libros, pero renombrando las columnas de salida como "nombre_libro" y "escritor".
SELECT titulo AS nombre_libro, autor AS escritor FROM  libros;

-- EJERCICIO 8.4 - Funciones de agregacion y relaciones (1 punto)
-- a) Escribe una consulta que muestre, por cada autor, la cantidad total de libros que tiene registrados (usa COUNT y GROUP BY).
SELECT autor, COUNT(titulo) FROM libros GROUP BY autor;

-- b) Escribe la sentencia SQL para crear una tabla intermedia llamada prestamos que relacione la tabla usuarios con la tabla libros (relacion muchos a muchos), incluyendo las llaves foraneas correspondientes (usuario_id y libro_id) tal como se trabajo en clase con la tabla alumnos_cursos.

CREATE TABLE prestamos(
    id SERIAL PRIMARY KEY,
	usuario_id INT REFERENCES usuarios(id),
	libro_id INT REFERENCES libros(id)
);

INSERT INTO prestamos (usuario_id, libro_id)
VALUES
(1,2),
(1,3),
(2,1),
(2,2),
(3,3),
(3,1),
(4,3),
(4,4);

-- EJERCICIO 8.5 - JOIN, LEFT JOIN, RIGHT JOIN (2 puntos)
-- Usando la tabla prestamos creada en el ejercicio anterior (prestamos, con las columnas usuario_id y libro_id) junto con las tablas usuarios y libros, escribe las siguientes consultas SQL:

-- a) Usando JOIN (INNER JOIN), muestra el nombre del usuario junto con el titulo del libro, solo para los prestamos que efectivamente existen (usuarios que si tienen algun libro prestado).

SELECT u.nombre, l.titulo
FROM prestamos p
INNER JOIN usuarios u ON p.usuario_id = u.id
INNER JOIN libros l oN p.libro_id = l.id;

-- b) Usando LEFT JOIN, muestra el nombre de TODOS los usuarios junto con el titulo del libro que tienen prestado (si un usuario no tiene ningun prestamo, el titulo debe aparecer como NULL).
SELECT u.nombre, l.titulo
FROM usuarios u
LEFT JOIN prestamos p ON u.id = p.usuario_id
LEFT JOIN libros l ON p.libro_id = l.id;

-- c) Usando RIGHT JOIN, muestra el titulo de TODOS los libros junto con el nombre del usuario que los tiene prestados (si un libro nunca fue prestado, el nombre del usuario debe aparecer como NULL).
SELECT l.titulo, u.nombre
FROM usuarios u
RIGHT JOIN prestamos p ON u.id = p.usuario_id
RIGHT JOIN libros l ON p.libro_id = l.id;

-- d) Usando JOIN entre las 3 tablas y una funcion de agregacion, escribe una consulta que muestre, por cada usuario, la cantidad de libros que tiene actualmente en prestamo (usa COUNT y GROUP BY sobre el nombre del usuario).

SELECT u.nombre, COUNT(l.id) AS libros_prestados
FROM usuarios u
FULL OUTER JOIN prestamos p ON u.id = p.usuario_id
FULL OUTER JOIN libros l ON p.libro_id = l.id
GROUP BY u.nombre;