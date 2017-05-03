# Script de criação do banco de dados.

DROP DATABASE Uniwallet;
CREATE DATABASE Uniwallet;

USE Uniwallet;

CREATE TABLE Users (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	fullname VARCHAR(128) NOT NULL,
	email VARCHAR(64) NOT NULL,
	password VARCHAR(128) NOT NULL,
	university VARCHAR(64) NOT NULL,
	cpf VARCHAR(64) NOT NULL
);

CREATE TABLE AccessLevels (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(32) NOT NULL,
	description VARCHAR(256)
);

INSERT INTO AccessLevels (name, description) VALUES ('registered', 'Basic access level for everyone by default');

CREATE TABLE User_AccessLevel (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	accesslevel_id INT(32) UNSIGNED NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(id),
	FOREIGN KEY (accesslevel_id) REFERENCES AccessLevels(id)
);

CREATE TABLE AuthSession (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	token VARCHAR(256) NOT NULL,
	ip VARCHAR(128) NOT NULL,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Companies (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	email VARCHAR(64) NOT NULL,
	login VARCHAR(64) NOT NULL,
	password VARCHAR(128) NOT NULL,
	ddd VARCHAR(32),
	phone VARCHAR(32),
	address VARCHAR(128),
	city VARCHAR(128),
	cnpj VARCHAR(32)
);
