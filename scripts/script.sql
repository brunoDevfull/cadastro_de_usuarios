MY SQL SCRIPT db_cadastros

create database cadastros;

use cadastros;

CREATE TABLE usuarios (
    login VARCHAR(50) NOT NULL,
    senha VARCHAR(255) NOT NULL
);

drop table usuarios;


INSERT INTO usuarios (login, senha) VALUES ('admin', SHA2('admin', 256));


SELECT * FROM usuarios;