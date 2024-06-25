--create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--create the user if not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* to 'hbnb_test'@'localhost';

--grant select priviledges on performance schema to hbnb_test
GRANT SELECT ON performance_schema.* to 'hbnb_test'@'localhost';

--flush the privileges
FLUSH PRIVILEGES;