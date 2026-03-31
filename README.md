# Equistock - Technical test for the position of Full Stack Developer at Voltaire Group

This project is a mini fullstack back-office application designed to manage a product catalog (saddles, stirrups, and accessories).

It showcases:

- clean architecture
- thoughtful technical decisions
- best practices in code organization and version control

## Tech Stack

### Backend - FastAPI (Pyhton + Uvicorn)

I chose FastAPI for:

- high performance
- simplicity and readability
- strong type safety with Python type hints
- automatic API documentation (Swagger / OpenAPI)

Node.js would also be a valid option, but I am more familiar with FastAPI, which allowed me to be more efficient and focus on code quality.

### Database - PostgreSQL

I chose PostgreSQL because:

- the product catalog has a clear relational structure (products, categories, stock)
- it ensures strong data integrity (constraints, types, relations)
- it is well-suited for structured queries and scalability

MongoDB is more appropriate for unstructured or flexible data, which is not the case here.

### Frontend - Vue 3 (Vite)

I chose Vue 3 for:

- its simplicity and readability
- a built-in reactivity system
- a structured ecosystem (routing, state management, testing)
- fast setup with minimal boilerplate

Compared to React, Vue is more opinionated and quicker to implement for this type of project.
Compared to vanilla JavaScript, it provides better structure and maintainability.

Angular would also be a good option, but heavier for this scope and less flexible in terms of customization.

### Orchestration - Docker

The project uses Docker Compose to:

- simplify environment setup
- ensure consistency across development environments
- run backend, database and frontend services together

## Repository structure

- `backend/`
  - `app/main.py`: FastAPI app
  - `requirements.txt`
  - `Dockerfile`
- `data/` (database container build files)
- `frontend/`
  - Vue app + `Dockerfile`
  - `package.json`
  - `vite.config.ts`
- `docker-compose.yml`

## Getting Started

### Prerequisites

- **Docker** and **Docker Compose**
- **Git**
- **Node.js** (optional, for local frontend linting).
- **Python 3.10+** (optional, for local backend linting).

### Installation & Setup

#### Clone the repository

```bash
git clone https://github.com/cdorignac/voltaire-groupe-test-technique.git
cd voltaire-groupe-test-technique
```

#### Setup environment variables

Create a `.env` file in the root directory (refer to .env.example).

### Launch the application

```bash
docker compose up --build
```

Once the containers are running, you can access the services at:

    - Backend: `http://localhost:8000`
    - OpenAPI docs: `http://localhost:8000/docs`
    - Frontend: `http://localhost:3000`

### Local development (outside Docker)

#### Backend

1. `cd backend`
2. `python -m venv .venv`
3. `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac)
4. `pip install -r requirements.txt`
5. `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

#### Frontend

1. `cd frontend`
2. `npm install`
3. `npm run dev`
4. Open `http://localhost:5173`

### Tests

#### Backend

1. `cd backend`
2. `python -m venv .venv`
3. `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac)
4. `pip install -r requirements.txt`
5. `pytest app/tests/ -v`

