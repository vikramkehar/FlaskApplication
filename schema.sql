-- # Create tables in MYSQL workbench.

-- # //Table Schema for user:

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    projectid INT
);


-- # //Table Schema for project:

CREATE TABLE project (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(80) UNIQUE NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    alloted_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);