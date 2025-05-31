# PostgreSQL Docker Container

This directory contains files to build and run a PostgreSQL database in a Docker container.

## Files

- `Dockerfile`: Instructions for building the PostgreSQL container
- `init.sql`: SQL script to initialize the database schema and sample data
- `docker-compose.yml`: Configuration for running the PostgreSQL container

## How to Run

1. Make sure you have Docker and Docker Compose installed
2. Navigate to this directory
3. Run the PostgreSQL container:

```bash
docker-compose up
```

4. The PostgreSQL server will be available at localhost:5432

## Connection Details

- **Host**: localhost (or postgres-db from other containers in the same Docker Compose setup)
- **Port**: 5432
- **Database**: postgres
- **Username**: postgres
- **Password**: postgres

## Connecting from Another Container

When using Docker Compose, all services are automatically on the same network and can communicate using service names. Use `postgres-db` as the hostname when connecting from another service in the same Docker Compose setup.