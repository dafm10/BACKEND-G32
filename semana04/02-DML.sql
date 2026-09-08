-- DML : Data Manipulation Language (Lenguaje de Manipulación de Datos)
\c pruebas -- entramos a la BD pruebas

-- INSERT : Ingresar nuevos registros a una tabla en particular
-- SELECT : Obtener la información de determinados registros de una o varias tablas
-- UPDATE : Actualizar la información registrada
-- DELETE : Elimina de manera permanete los registro en base a condiciones

-- INSERT INTO nombre_tabla (nomb_col_1, nomb_col_2, ...) VALUES (val_1, val_2, ...);

INSERT INTO personas (id, nombre, apellido, correo, fecha_nacimiento) VALUES
-- DEFAULT > Indicamos el valor por defecto definido en la columna
-- En las columnas SERIAL agarra el valor que le toca
-- En SQL comillas simples para información de texto
-- Comiillas dobles para nombres de tablas, columnas, etc
-- En SQL se usa el ISO-8601 para las fechas, en el cual el formato es: YYY-MM-DD HM:NN:SS:mmmm
                    (DEFAULT, 'Eduardo', 'De Rivero', 'ederiveroman@gmail.com', '1999-12-31');

-- Si voy a insertar usando el orden de las columnas con el que la cree, puedo prescindir del nombre de las columnas, PERO si o si tengo que declarar todas las columnas
INSERT INTO personas VALUES (DEFAULT, 'Martha', 'Escobedo', 'mescobedo@gmail.com', '2005-02-14'),
                            (DEFAULT, 'Rodrigo', 'Jimenez', 'rjimenez@gmail.com', '1989-06-15'),
                            (DEFAULT, 'Marge', 'Marquez', 'mmarquez@gmail.com', '2006-09-07');



-- Volviendo al DDL, ALTER (Modificar la tabla)
-- Agregar columnas
-- Siempre irá al final, no se puede modificar el orden, si se puede hacer en MySQL, MariaDB
-- ALTER TABLE personas add COLUMN sexo TEXT BEFORE | AFTER id;
ALTER TABLE personas ADD COLUMN sexo TEXT;

-- Eliminar columnas
ALTER TABLE personas DROP COLUMN fecha_nacimiento;

-- Cambiar el tipo de dato
-- Si vamos a cambiar de TEXT a INT entonces debemos de corroborar el cambio
ALTER TABLE personas ALTER COLUMN sexo TYPE INT USING sexo::INT;

-- Renombrar la columna
ALTER TABLE personas RENAME COLUMN sexo TO peso;