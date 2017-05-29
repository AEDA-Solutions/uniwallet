# Script de criação do banco de dados.

DROP DATABASE IF EXISTS Uniwallet;
CREATE DATABASE Uniwallet;

USE Uniwallet;
CREATE TABLE Users (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
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

INSERT INTO Users (name, email, password) VALUES
('Uniwallet team', 'team@team.com', 'uniwallet');

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

INSERT INTO Consumers (user_id, fullname, university, cpf) VALUES
('1', 'Uniwallet da Silva', 'UnB', 'Sim');

CREATE TABLE Companies (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	name VARCHAR(128) NOT NULL,
	cnpj VARCHAR(32),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

INSERT INTO Companies (user_id, name, cnpj) VALUES
('1', 'Uniwallet_Corporation', 'SIM');

CREATE TABLE Wallets (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	user_id INT(32) UNSIGNED NOT NULL,
	balance DOUBLE UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (user_id) REFERENCES Users(id)
);

INSERT INTO Wallets (user_id, balance) VALUES
('1', '1000');

CREATE TABLE Stores (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(128) NOT NULL,
	company_id INT(32) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (company_id) REFERENCES Companies(id)
);

INSERT INTO Stores (name, company_id) VALUES
('Uni_store', '1');

CREATE TABLE Categories (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	company_id INT(32) UNSIGNED NOT NULL,
	name VARCHAR(128) NOT NULL,
	description VARCHAR(256) NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Products (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	company_id INT(32) UNSIGNED NOT NULL,
	number INT(32) UNSIGNED NOT NULL, #associa com a loja? com o codigo do comerciante?
	name VARCHAR(128) NOT NULL,
	description VARCHAR(256) NOT NULL,
	category VARCHAR(128) NOT NULL,
	price DOUBLE UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (company_id) REFERENCES Companies(id)
);

CREATE TABLE Product_Category (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id INT(32) UNSIGNED NOT NULL,
	category_id INT(32) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (product_id) REFERENCES Products(id),
	FOREIGN KEY (category_id) REFERENCES Categories(id)
);

CREATE TABLE Product_Prices (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id INT(32) UNSIGNED NOT NULL,
	price DOUBLE UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (product_id) REFERENCES Products(id)
);

CREATE TABLE Sales (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	consumer_id INT(32) UNSIGNED NOT NULL,
	company_id INT(32) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (consumer_id) REFERENCES Consumers(id),
	FOREIGN KEY (company_id) REFERENCES Companies(id)
);

CREATE TABLE Sale_Product (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id INT(32) UNSIGNED NOT NULL,
	sale_id INT(32) UNSIGNED NOT NULL,
	quantity INT(128) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (product_id) REFERENCES Products(id),
	FOREIGN KEY (sale_id) REFERENCES Sales(id)
);

INSERT INTO Products (company_id, number, name, price, description, category) VALUES
('1', '123', 'Pão Gostoso', '75.50', 'Gostoso', 'Alimentos');

INSERT INTO Product_Prices (product_id, price) VALUES
('1', '65.50');

CREATE TABLE Product_Store (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	product_id INT(32) UNSIGNED NOT NULL,
	store_id INT(32) UNSIGNED NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (product_id) REFERENCES Products(id),
	FOREIGN KEY (store_id) REFERENCES Stores(id),
	UNIQUE (product_id, store_id)
);

CREATE TABLE Transactions (
	id INT(32) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	destiny INT(32) UNSIGNED NOT NULL,
	operation VARCHAR(32) NOT NULL,
	value INT(32),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (consumer_id) REFERENCES Consumers(id),
	FOREIGN KEY (company_id) REFERENCES Companies(id)
);