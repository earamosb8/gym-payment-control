-- create database
CREATE DATABASE halofit;

--UTILIZANDO DATABASE
use halofit;

--create table cliente

CREATE TABLE IF NOT EXISTS cliente (
    id INT(20) UNSIGNED,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono INT(20) UNSIGNED,
    fecha date NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS users (
    id INT(3) UNSIGNED UNIQUE,
    user VARCHAR(50) NOT NULL,
    pass VARCHAR(50) NOT NULL,
    PRIMARY KEY (user)
);

