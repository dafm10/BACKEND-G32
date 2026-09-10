-- Continuando con el DML
-- UPDATE > actualizar los registros de las tablas
-- Si en el UPDATE no se pone condicionales, se modificarán todos los registros.
-- UPDATE nombre_tabla SET nombre = 'Ayudin' WHERE id = X
UPDATE productos SET nombre = 'Arroz Faraon 5k' WHERE id = 1;

-- Cada vez que se actualiza un registro, este NO VARIA su ubicación de memoria pero modifica el índice del registro que hace que se muestre al final

-- para actualizar sin usar el ID
UPDATE productos SET nombre = 'Cerveza Cusqueña 620ml' WHERE nombre LIKE 'Cerveza Cusqueña 620ml';



-- DELETE
-- Elimina los datos de manera permanente de mi tabla o mis registros
-- DELETE FROM nombre_tabla WHERE condicionales;
DELETE FROM productos WHERE id = 9;

-- La única forma de revertir los cambios (UPDATE ó DELETE) es si la query está en una transacción