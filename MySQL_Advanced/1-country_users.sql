-- Task 1 : SQL script that creates table 'users' with enumeration constraints

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country enumeration("US", "CO", "TN") NOT NULL DEFAULT "US"
);
