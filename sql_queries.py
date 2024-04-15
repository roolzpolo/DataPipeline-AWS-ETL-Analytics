DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS categoria (
    idcategoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255),
    estado BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS rol (
    idrol SERIAL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(255),
    estado BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
    idusuario SERIAL PRIMARY KEY,
    idrol INTEGER NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50) NOT NULL,
    clave VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    CONSTRAINT fk_usuario_rol FOREIGN KEY (idrol) REFERENCES rol (idrol)
);

CREATE TABLE IF NOT EXISTS persona (
    idpersona SERIAL PRIMARY KEY,
    tipo_persona VARCHAR(20) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20),
    num_documento VARCHAR(20),
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS venta (
    idventa SERIAL PRIMARY KEY,
    idcliente INTEGER NOT NULL,
    idusuario INTEGER NOT NULL,
    tipo_comprobante VARCHAR(20) NOT NULL,
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10) NOT NULL,
    fecha TIMESTAMP NOT NULL,
    impuesto NUMERIC(4, 2) NOT NULL,
    total NUMERIC(11, 2) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    CONSTRAINT fk_venta_cliente FOREIGN KEY (idcliente) REFERENCES persona (idpersona),
    CONSTRAINT fk_venta_usuario FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);

CREATE TABLE IF NOT EXISTS articulo (
    idarticulo SERIAL PRIMARY KEY,
    idcategoria INTEGER NOT NULL,
    codigo VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio_venta NUMERIC(11, 2) NOT NULL,
    stock INTEGER NOT NULL,
    descripcion VARCHAR(255),
    imagen VARCHAR(20),
    estado BOOLEAN NOT NULL,
    CONSTRAINT fk_articulo_categoria FOREIGN KEY (idcategoria) REFERENCES categoria (idcategoria)
);

CREATE TABLE IF NOT EXISTS detalle_venta (
    iddetalle_venta SERIAL PRIMARY KEY,
    idventa INTEGER NOT NULL,
    idarticulo INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio NUMERIC(11, 2) NOT NULL,
    descuento NUMERIC(11, 2) NOT NULL,
    CONSTRAINT fk_detalle_venta_venta FOREIGN KEY (idventa) REFERENCES venta (idventa),
    CONSTRAINT fk_detalle_venta_articulo FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

CREATE TABLE IF NOT EXISTS ingreso (
    idingreso SERIAL PRIMARY KEY,
    idproveedor INTEGER NOT NULL,
    idusuario INTEGER NOT NULL,
    tipo_comprobante VARCHAR(20) NOT NULL,
    serie_comprobante VARCHAR(7),
    num_comprobante VARCHAR(10) NOT NULL,
    fecha TIMESTAMP NOT NULL,
    impuesto NUMERIC(4, 2) NOT NULL,
    total NUMERIC(11, 2) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    CONSTRAINT fk_ingreso_proveedor FOREIGN KEY (idproveedor) REFERENCES persona (idpersona),
    CONSTRAINT fk_ingreso_usuario FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);

CREATE TABLE IF NOT EXISTS detalle_ingreso (
    iddetalle_ingreso SERIAL PRIMARY KEY,
    idingreso INTEGER NOT NULL,
    idarticulo INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio NUMERIC(11, 2) NOT NULL,
    CONSTRAINT fk_detalle_ingreso_ingreso FOREIGN KEY (idingreso) REFERENCES ingreso (idingreso),
    CONSTRAINT fk_detalle_ingreso_articulo FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

'''