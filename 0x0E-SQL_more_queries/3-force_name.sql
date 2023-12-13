-- Script that creates the table force_name on your MySQL server.

-- Use the hbtn_0d_2 database
USE hbtn_0d_2;

-- Create table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
);
