-- En bases de datos relaciones, existen 3 tipos de relaciones entre tablas
-- 1 a 1 => es una relación en la cual 2 tablas tendrán un registro que represente a la otra en un solo registro
-- Usuario tiene una persona
-- La clave foranea > es la representación del registro (PK) de la tabla A hacia la tabla B
-- La clave foránea (FK) no importa en cual de las 2 tablas vaya por que es 1 a 1

-- 1 a n (muchos) => una persona puede tener varias direcciones
-- La FK va en la tabla "varias", en este escenario la fk iría en la tabla de direcciones. Por qué asi se representa que ese registro le pertenece a una persona determinada

-- n a m (muchos) =>
-- Alumno tiene varios cursos
-- Curso tiene varios alumnos
-- Al tener una relación de muchos a muchos la FK no puede existir en alguna de las tablas y por ende se crea una tabla Intermedia ó Pivote ó Puente, en la cual en esa tabla iran las FK de las dos tablas (fk_alumno, fk_curso)


CREATE DATABASE directorio;
\c directorio;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    correo TEXT UNIQUE
);

-- Si hemos ejecutado la creación de la tabla direcciones, por el ejercicio, hay que eliminarla con el DROP
DROP TABLE direcciones;

CREATE TABLE direcciones (
    id SERIAL PRIMARY KEY,
    calle TEXT NOT NULL,
    numero TEXT,
    referencia TEXT,
    distrito TEXT,
    -- Si la columna que será utilizada para la relación es UNIQUE, entonces es relación de 1-1 si no, 1 a muchos
    usuario_id INT, -- Esta es una columna normal, la relación se crea en la siguiente línea
    -- ASI SE AGREGA LA LLAVE FORANEA EN UNA RELACIÓN DE 1-n
    CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

SELECT * FROM direcciones;



--------------------
-- Muchos a muchos
CREATE TABLE alumnos (
    id SERIAL PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nombre TEXT
);

CREATE TABLE alumnos_cursos (
    alumno_id INT,
    curso_id INT,
    CONSTRAINT fk_alumno FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
    -- Al ser una tabla puente | pivote se crea una PRIMARY KEY compuesta
    PRIMARY KEY (alumno_id, curso_id)
);