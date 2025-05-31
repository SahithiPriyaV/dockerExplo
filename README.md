# PostgreSQL and Flask Docker Setup

This project demonstrates how to run a Flask application and PostgreSQL database in separate Docker containers, with the Flask app performing CRUD operations on the PostgreSQL database.

## Project Structure

- `pythonApp/`: Contains the Flask application
  - `app.py`: Flask API with PostgreSQL CRUD operations
  - `Dockerfile`: Instructions for building the Flask application container
  - `requirements.txt`: Python dependencies
- `sqlengine/`: Contains the PostgreSQL database setup
  - `Dockerfile`: Instructions for building the PostgreSQL container
  - `init.sql`: SQL script to initialize the database schema
- `docker-compose.yml`: Configuration for running both containers
- `test_api.py`: Script to test the API endpoints

## How to Run

1. Make sure you have Docker and Docker Compose installed
2. Navigate to the project directory
3. Run the application with Docker Compose:

```bash
docker-compose up
```

4. The API will be available at http://localhost:5000

## API Endpoints

- `GET /setup`: Initialize the database and create the users table
- `GET /users`: Get all users
- `GET /users/{id}`: Get a specific user by ID
- `POST /users`: Create a new user (requires JSON body with name and email)
- `PUT /users/{id}`: Update a user (requires JSON body with fields to update)
- `DELETE /users/{id}`: Delete a user

## Testing

You can run the included test script to verify all API endpoints:

```bash
python test_api.py
```

## Container Architecture

- **postgres-db**: PostgreSQL database container
  - Exposes port 5432
  - Uses a named volume for data persistence
  - Configured with health checks

- **flask-app**: Flask application container
  - Exposes port 5000
  - Connects to the PostgreSQL container using the service name
  - Mounts a volume for logs

Docker Compose automatically creates a default network for all services, allowing them to communicate using service names.