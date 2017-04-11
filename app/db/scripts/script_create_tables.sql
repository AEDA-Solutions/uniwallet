# Script de criação do banco de dados.

CREATE DATABASE Uniwallet;

USE Uniwallet;

CREATE TABLE Users (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(30) NOT NULL,
	lastname VARCHAR(30) NOT NULL,
	email VARCHAR(50) NOT NULL,
	university VARCHAR(50) NOT NULL,
	password VARCHAR(20) NOT NULL
);


