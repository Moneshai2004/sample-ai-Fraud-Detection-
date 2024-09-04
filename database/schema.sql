-- database/schema.sql
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT,
    amount FLOAT,
    timestamp BIGINT,
    location VARCHAR(255),
    merchant VARCHAR(255),
    is_fraud BOOLEAN
);
