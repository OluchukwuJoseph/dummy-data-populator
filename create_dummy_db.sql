CREATE DATABASE IF NOT EXISTS dummy;
USE dummy;
CREATE TABLE IF NOT EXISTS person (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  firstname VARCHAR(50),
  lastname VARCHAR(50),
  age INTEGER
);
