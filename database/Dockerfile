FROM postgres:18-alpine

# Set environment variables for PostgreSQL configuration
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

EXPOSE 5432

VOLUME ["/var/lib/postgresql/data"]