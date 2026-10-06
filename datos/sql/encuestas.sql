CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    nacionalidad VARCHAR(50),
    telefono VARCHAR(15),
    tipo VARCHAR(20),
    contraseña VARCHAR(255) NOT NULL,
    empresa VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    edad INT,
    genero VARCHAR(10),
    vinculo VARCHAR(20)

) COMMENT 'Tabla que almacena la informacion de los usuarios';

CREATE TABLE encuesta (
    id_encuesta INT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_cierre TIMESTAMP NULL,
    id_empresa INT NOT NULL,
    id_usuario INT,
    activo BOOLEAN DEFAULT TRUE,
    grupo_interes VARCHAR(100),
    privada_permitida BOOLEAN DEFAULT FALSE,
    id_recompensa INT,
    CONSTRAINT fk_encuesta_empresa
        FOREIGN KEY (id_empresa) REFERENCES empresa (id_empresa),
    CONSTRAINT fk_encuesta_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    CONSTRAINT fk_encuesta_recompensa
        FOREIGN KEY (id_recompensa) REFERENCES recompensa (id_recompensa)
) COMMENT 'Tabla que almacena la informacion de las encuestas';


CREATE TABLE empresa (
    id_empresa INT PRIMARY KEY,
    nombre_empresa VARCHAR(100) NOT NULL,
    direcion VARCHAR(255),
    telefono VARCHAR(15),
    correo_electronico VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mercado_empresa VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE
) COMMENT 'Tabla que almacena la informacion de la empresa';

CREATE TABLE recompensa (
    id_recompensa INT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    duracion_dias INT COMMENT 'Dias disponibles para obtener o canjear la recompensa',
    requisitos VARCHAR(255),
    activo BOOLEAN DEFAULT TRUE,
    registro_recompensa BOOLEAN DEFAULT TRUE
) COMMENT 'Tabla que almacena los tipos de recompensa de las encuestas';


CREATE TABLE requisitos (
    id_requisitos INT PRIMARY KEY,
    descripcion VARCHAR(255),
    activo BOOLEAN DEFAULT TRUE,
    vinculo VARCHAR(20)
) comment 'Tabla que re representa los requisitos de las recompensas';



