CREATE TABLE Usuario(
    ID INT UNIQUE AUTO_INCREMENT,
    nombre_usuario VARCHAR(20),
    correo_usuario VARCHAR(30),
    password_usuario VARCHAR(255),
    fecha_creacion_usuario DATE DEFAULT (CURDATE()),
    PRIMARY KEY(ID)
);
CREATE TABLE Categoria(
    ID_categoria INT AUTO_INCREMENT,
    nombre_categoria VARCHAR(50),
    categoria_padre VARCHAR(50),
    PRIMARY KEY(ID_categoria)
);
CREATE TABLE Articulo(
    ID INT AUTO_INCREMENT,
    nombre_articulo VARCHAR(50),
    precio_kilo VARCHAR(30),
    peso_articulo VARCHAR(30),
    precio_articulo VARCHAR(20),
    marca_articulo VARCHAR(30),
    ID_categoria INT(5),
    FOREIGN KEY(ID_categoria) REFERENCES Categoria(ID_categoria),
    PRIMARY KEY(ID)
);