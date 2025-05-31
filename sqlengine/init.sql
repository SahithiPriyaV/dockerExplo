-- Initialize database schema

-- Create users table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO users (name, email, age) VALUES
    ('John Doe', 'john.doe@example.com', 30),
    ('Jane Smith', 'jane.smith@example.com', 25)
ON CONFLICT (email) DO NOTHING;