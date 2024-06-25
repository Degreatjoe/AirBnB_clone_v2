-- Create the database if it doesn't exist
CREATE database if not EXISTS hbnb_dev_db;

-- Create the user if it doesn't exist, and set the password
CREATE user if not EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';

-- Grant select privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* to 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
