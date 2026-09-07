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

-- Sirve para ejecutar cualquier comando de la termina fuera de postgres
-- Limpiaremos la terminal
\! clear
\! cls

-- Creamos una tabla
CREATE TABLE PERSONAS (
    -- Ahora definimos las columnas que contendrá la tabla
    -- nombre_columna tipo_de_Dato opciones_adicionales
    id SERIAL PRIMARY KEY, -- Solmanete debe existir una columna SERIAL en toda la tabla
    -- UNIQUE > Indica que un registro no pueda tener el mismo valor de otro registro
    -- NOT NULL > Indica que la columna jamás podrá tener valores nulos
    -- NULL > Si podrá tener valores nulos (configuración por defecto)
    -- PRIMARY KEY > Indica que la columan será escogida como representación del registro y se usará para encontrar el registro más rápido, acá generalmente suelen ser los ID's
    -- DEFAULT valor > Indica que al momento de registrar o actualizar el valor de la columna, si no se ingresa nada se pondrá el valor con valor predeterminado.
    nombre TEXT NOT NULL, -- TEXT no tiene límites, es decir podemos almacenar grandes cantidades de texto y este variará su almacenamiento en base al texto almacenado.
    apellido VARCHAR(50), -- VARCHAR es variado en almacenamiento
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento TIMESTAMP WITH TIME ZONE
);

-- Para ver las tablas creadas en la BD
\dt

-- Para ver las tablas y las secuenciales (autoincrementables) creadas en la base de datos
\d

-- Nos mostrará la definición de toda la configuración de esa table y en la parte de abajo mostrará sus indices
\d NOMBRE_TABLA