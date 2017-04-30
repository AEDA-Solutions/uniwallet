# Script de criação do banco de dados.

DROP DATABASE ArthurDatabase;
CREATE DATABASE ArthurDatabase;

USE ArthurDatabase;

CREATE TABLE Cebolitos (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(128) NOT NULL,
	email VARCHAR(64) NOT NULL,
	senha VARCHAR(128) NOT NULL
);

