CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nacionalidad VARCHAR(50),
    telefono NUMBER(15),
    tipo VARCHAR(20),
    contraseña VARCHAR(255) NOT NULL,
    empresa VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    edad INT,
    genero VARCHAR(10)
) COMENT 'Tabla de registro para usuario de app de encuestas.';