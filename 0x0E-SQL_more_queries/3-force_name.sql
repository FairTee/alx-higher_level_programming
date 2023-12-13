-- Create the force_name table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert data only if it doesn't exist
INSERT INTO force_name (id, name) VALUES (89, 'Best School') 
ON DUPLICATE KEY UPDATE name = VALUES(name);
