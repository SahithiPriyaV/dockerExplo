# Use official PostgreSQL image as base
FROM postgres:14

# Set environment variables (can be overridden at runtime)
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

# Copy initialization scripts if needed
COPY init.sql /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432

# # Data directory will be a volume by default
# VOLUME /var/lib/postgresql/data