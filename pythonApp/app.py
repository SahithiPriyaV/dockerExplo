"""
Flask API for PostgreSQL CRUD Operations
"""
import os
import logging
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("host_logs/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Database connection parameters
DB_HOST = os.environ.get('DB_HOST', 'postgres-db')
DB_PORT = int(os.environ.get('DB_PORT', 5432))
DB_NAME = os.environ.get('DB_NAME', 'postgres')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')

def get_db_connection():
    """Create a database connection"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {e}")
        return None

def setup_database():
    """Create users table if it doesn't exist"""
    try:
        conn = get_db_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) UNIQUE NOT NULL,
                        age INTEGER,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
            conn.close()
            logger.info("Database setup complete")
            return True
        return False
    except Exception as e:
        logger.error(f"Database setup error: {e}")
        return False

@app.route('/')
def index():
    return jsonify({"message": "PostgreSQL CRUD API is running"})

@app.route('/setup', methods=['GET'])
def init_db():
    if setup_database():
        return jsonify({"message": "Database setup complete"})
    return jsonify({"error": "Database setup failed"}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        
        conn.close()
        return jsonify(list(users))
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()
        
        conn.close()
        
        if user:
            return jsonify(dict(user))
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        if not data or not all(key in data for key in ['name', 'email']):
            return jsonify({"error": "Name and email are required"}), 400
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (name, email, age) VALUES (%s, %s, %s) RETURNING id",
                (data.get('name'), data.get('email'), data.get('age'))
            )
            user_id = cursor.fetchone()[0]
        
        conn.close()
        return jsonify({"id": user_id, "message": "User created successfully"}), 201
    except psycopg2.errors.UniqueViolation:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        set_clause = []
        values = []
        
        if 'name' in data:
            set_clause.append("name = %s")
            values.append(data['name'])
        
        if 'email' in data:
            set_clause.append("email = %s")
            values.append(data['email'])
        
        if 'age' in data:
            set_clause.append("age = %s")
            values.append(data['age'])
        
        if not set_clause:
            return jsonify({"error": "No valid fields to update"}), 400
        
        values.append(user_id)
        
        with conn.cursor() as cursor:
            cursor.execute(
                f"UPDATE users SET {', '.join(set_clause)} WHERE id = %s RETURNING id",
                tuple(values)
            )
            updated = cursor.fetchone()
        
        conn.close()
        
        if updated:
            return jsonify({"message": "User updated successfully"})
        return jsonify({"error": "User not found"}), 404
    except psycopg2.errors.UniqueViolation:
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        logger.error(f"Error updating user: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({"error": "Database connection failed"}), 500
        
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s RETURNING id", (user_id,))
            deleted = cursor.fetchone()
        
        conn.close()
        
        if deleted:
            return jsonify({"message": "User deleted successfully"})
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)