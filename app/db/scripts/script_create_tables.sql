# Script de criação do banco de dados.

CREATE DATABASE Uniwallet;

USE Uniwallet;

CREATE TABLE Users (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
login VARCHAR(10) NOT NULL,
password VARCHAR(20) NOT NULL,
ddd INT(2),
cellphone INT(9),
address VARCHAR(100),
city VARCHAR(20),
state VARCHAR(20),
neighborhhood VARCHAR(20),
cpf INT(11)
);

CREATE TABLE Company (
companyid INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
companyname VARCHAR(30) NOT NULL,
companyemail VARCHAR(50) NOT NULL,
companylogin VARCHAR(15) NOT NULL,
companypassword VARCHAR(15) NOT NULL,
companyddd INT(2),
companyphone INT(9),
companyaddress VARCHAR(100)
city VARCHAR(20),
cnpj INT(14)
);


);
