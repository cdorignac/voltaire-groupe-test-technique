FROM postgres:17-alpine

# Set environment variables for PostgreSQL configuration
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

EXPOSE 5432

COPY ./create_table.sql /docker-entrypoint-initdb.d/
COPY ./sample_data.sql /docker-entrypoint-initdb.d/

VOLUME ["/var/lib/postgresql/data"]