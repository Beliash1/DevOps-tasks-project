# DevOps Tasks Project

A simple Flask + PostgreSQL task manager API, built as a hands-on project to learn Docker, Jenkins, and CI/CD from scratch.

I wanted to actually understand how the pieces fit together — not just read about them — so this project focuses more on the DevOps workflow than on the app itself. The app is intentionally simple (basic CRUD for tasks); the real work is in how it gets built, tested, and deployed.

## What's here

- **Flask backend** (`backend/`) — a small REST API for managing tasks (create, read, update, delete)
- **PostgreSQL** — running as a separate container, connected via Docker Compose
- **Docker** — the app and database are fully containerized
- **Jenkins** — a full CI/CD pipeline that builds, tests, pushes to Docker Hub, and deploys automatically

## Tech stack

- Python / Flask
- PostgreSQL
- Docker & Docker Compose
- Jenkins (Pipeline as Code via Jenkinsfile)

## How the pipeline works

Every push to main triggers Jenkins to:

1. Pull the latest code from this repo
2. Build a Docker image for the backend
3. Run a basic sanity check on it
4. Push the image to Docker Hub
5. Redeploy the containers with docker compose

## Running it locally

git clone https://github.com/Beliash1/DevOps-tasks-project.git
cd DevOps-tasks-project
docker compose up --build

The API will be available at http://localhost:5000.

### Endpoints

| Method | Endpoint      | Description         |
|--------|---------------|----------------------|
| GET    | /health       | Health check         |
| GET    | /tasks        | List all tasks       |
| POST   | /tasks        | Create a new task    |
| PUT    | /tasks/<id>   | Update a task        |
| DELETE | /tasks/<id>   | Delete a task         |

## Why this project

I'm learning DevOps from the ground up and wanted a real (if small) project to practice on, instead of just following isolated tutorials. Things like credential scoping, container name conflicts, and flaky network pulls during builds — the stuff that doesn't show up until you actually run a pipeline yourself — taught me more than any single guide did.

## Status

Still a work in progress — next up is setting up automatic build triggers via GitHub webhooks, and eventually moving deployment to a real cloud environment.
