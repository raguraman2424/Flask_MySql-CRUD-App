create database project;

use project;

show tables;

create table users(
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
NAME VARCHAR(50),
AGE INT,
CITY VARCHAR(50)
);

SELECT*FROM USERS;

INSERT INTO USERS() VALUES
(1,'Ram',23,'Salem'),
(2,'Ravi',22,'banglore'),
(3,'Raman',21,'dharmapuri'),
(4,'Ragu',24,'krishnagri');