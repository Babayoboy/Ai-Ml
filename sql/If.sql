CREATE DATABASE learning; -- Tries to create database if esists thowrs error
CREATE DATABASE IF NOT EXISTS x;  -- Tries to create database only if database does not exist

DROP DATABASE x;  -- Tries to drop database if it doesn't exist throws error
DROP DATABASE IF EXISTS x; -- Tries to drop database only if it exists

SHOW DATABASES; -- SHows the database that exist

use x;
SHOW TABLES; -- Shows all the tables that exists in a database

