-- En el archivo SQL solo se ejecutarán las lineas que no empiecen con -- (doble guión)
-- Asimismo en SQL (Structured Query Language) SIEMPRE debe termina la instrucción con ";" (punto y coma)
-- Cuando en la terminal aparece un '=' luego del nombre de usuario del servidor, esto significa que está esperando una nueva consulta
-- Cuando aparece un '-' significa que ya hemos empezado una consulta y está esperando o más indicaciones o la finalización
-- Cuando aparece una `'` ó `"`(comilla simple o doble) significa que he abierto una pero aún no le ha cerrado
-- en SQL no es lo mismo comilla simple que comilla doble, la comilla simple se usa para texto, es decir para mostrar o almacena texto, mientras que la comilla doble se usa para llamar a nombre de tablas, columnas y nombres reservados


-- Tenemos dos sub conjuntos de lenguajes
-- DDL : Data Definition Language (Lenguaje de Definición de Datos)

-- CREATE: Crear entidades (Bases de Datos, tablas, usuarios, columnas, trigger)
-- ALTER: Alterar (modificar) bases de datos, tablas, usuarios, etc
-- DROP: Eliminar de raíz de manera permanente las entidades (base de datos, tablas, etc)
-- TRUNCATE: Elimna la data dentro de la tabla sin eliminar la tabla
-- RENAME: Cambiar el nombre de las entidades

CREATE DATABASE pruebas;

-- Cuando utilizamos un comando de PSQL no estamos obligados a poner ";", es opcional
\c pruebas