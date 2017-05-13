# Script de criação do banco de dados.

DROP DATABASE IF EXISTS Uniwallet;
CREATE DATABASE Uniwallet;

USE Uniwallet;

CREATE TABLE Users (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(64) NOT NULL,
	password VARCHAR(128) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE AccessLevels (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(32) NOT NULL,
	description VARCHAR(256),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Users (email, password) VALUES
('team@team.com', 'uniwallet');

INSERT INTO AccessLevels (name, description) VALUES 
('registered', 'Basic access level for everyone logged by default'),
('consumer', 'Consumer access level'),
('company', 'Company access level'),
('god', 'Unlimited access');

CREATE TABLE User_AccessLevel (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	accesslevel_id INT(32) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id),
	FOREIGN KEY (accesslevel_id) REFERENCES AccessLevels(id)
);

INSERT INTO User_AccessLevel (user_id, accesslevel_id) VALUES
(1, 1),
(1, 4);


CREATE TABLE AuthSession (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	token VARCHAR(256) NOT NULL,
	ip VARCHAR(128) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Consumers (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	fullname VARCHAR(128) NOT NULL,
	university VARCHAR(64) NOT NULL,
	cpf VARCHAR(64) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Companies (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	name VARCHAR(128) NOT NULL,
	cnpj VARCHAR(32),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);
