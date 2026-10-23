CREATE DATABASE learning;

USE learning;

CREATE TABLE Students (
	roll_no INT,
	name VARCHAR(30),
	age INT
);

INSERT  INTO Students
VALUES
(101, "adam", 12),
(102, "bob", 14);

SELECT * FROM Students;