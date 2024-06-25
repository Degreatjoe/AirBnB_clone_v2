--create the database if it does not exist
CREATE database IF NOT EXISTS hbnb_test_db;

--create the user if not exist
CREATE user IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES on hbnb_test_db.* to 'hbnb_test'@'localhost';

--grant select priviledges on performance schema to hbnb_test
GRANT SELECT on performance_schema.* to 'hbnb_test'@'localhost';

--flush the privileges
FLUSH PRIVILEGES;