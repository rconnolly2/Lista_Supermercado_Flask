CREATE TABLE Usuario(
    ID INT UNIQUE AUTO_INCREMENT,
    nombre_usuario VARCHAR(20),
    correo_usuario VARCHAR(30),
    password_usuario VARCHAR(255),
    fecha_creacion_usuario DATE DEFAULT (CURDATE()),
    PRIMARY KEY(ID)
);

CREATE TABLE Categoria(
    ID INT UNIQUE AUTO_INCREMENT,
    nombre_categoria VARCHAR(15),
    categoria_padre VARCHAR(10),
    PRIMARY KEY(ID)
);

CREATE TABLE Articulo(
    ID INT UNIQUE AUTO_INCREMENT,
    nombre_articulo VARCHAR(30),
    precio_kilo VARCHAR(10),
    peso_articulo VARCHAR(10),
    precio_articulo VARCHAR(10),
    marca_articulo VARCHAR(25),
    categoria VARCHAR(20),
    CONSTRAINT fk_categoria
    FOREIGN KEY(categoria)
    REFERENCES Categoria(ID),
    PRIMARY KEY(ID)
);
