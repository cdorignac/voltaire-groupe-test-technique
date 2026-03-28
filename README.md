# voltaire-groupe-test-technique

A full-stack sample app for the test project using:

- FastAPI backend (Python + Uvicorn)
- PostgreSQL (Docker container)
- Vue 3 frontend (Vite)
- Docker Compose orchestration

## 1. Getting Started

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

## 2. Repository structure

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
