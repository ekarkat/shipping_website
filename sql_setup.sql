-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS ship_db;
CREATE USER IF NOT EXISTS 'shipit_user'@'localhost' IDENTIFIED BY 'shipit_pwd';
GRANT ALL PRIVILEGES ON `ship_db`.* TO 'shipit_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'shipit_user'@'localhost';
FLUSH PRIVILEGES;
