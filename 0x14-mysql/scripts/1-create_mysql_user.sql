-- Create a MySQL user: holberton_user on both web-01 and web-02 with the host name: localhost and password: projectcorrection280hbtn
-- Make sure that holberton_user has permission to check the primary/replica status of your databases
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
