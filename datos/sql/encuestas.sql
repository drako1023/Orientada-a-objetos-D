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
) COMENT 'Tavla que almacen la informacion de los usuario de app de encuestas';




CREATE TABLE encuesta (
    id_encuesta INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_cierre TIMESTAMP,
    empresa VARCHAR(100) NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    grupo_interes VARCHAR(100),
    privada_permitida VARCHAR(10),
    Recompensas VARCHAR(100)
) COMENT 'Tabla que almacena la informacion de la encuesta';