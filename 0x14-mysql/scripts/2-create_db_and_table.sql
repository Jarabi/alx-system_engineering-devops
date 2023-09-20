-- Create a database named tyrell_corp (only in web-01)
-- Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
-- Make sure that holberton_user has SELECT permissions on your table to check that the table exists and is not empty.
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 ( id INT, name VARCHAR(256) );
INSERT INTO nexus6 (id, name) VALUES(1, "Leon");
FLUSH PRIVILEGES;
