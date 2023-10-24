CREATE TABLE Usuario(
    ID INT UNIQUE AUTO_INCREMENT,
    nombre_usuario VARCHAR(20),
    correo_usuario VARCHAR(30),
    password_usuario VARCHAR(255),
    fecha_creacion_usuario DATE DEFAULT (CURDATE()),
    PRIMARY KEY(ID)
);