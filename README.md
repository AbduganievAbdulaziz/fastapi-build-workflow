# Simple FastAPI Demo

A minimal FastAPI application for testing **Dockerization** and **CI-based versioning workflows** using GitHub Actions.

This project is intentionally small and focused on learning infrastructure and automation rather than application features.

---

## 🚀 Local Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python ./src/app.py
```

The API will be available at:

```
http://localhost:8000
```

---

## 🐳 Dockerization

To test the Docker workflow:

```bash
# Build the image
docker build -t fastapi-app .

# Run the container
docker run -d -p 8000:8000 fastapi-app
```

---

## 🔁 CI Workflow Scope

The GitHub Actions workflow in this repository focuses on **Continuous Integration (CI)**:

* building the application
* updating the application version
* creating patch/release branches from `main`

No deployment or publishing is performed.

---

## 📦 Endpoints

* `GET /` – returns status and current version
* `GET /health` – simple health check
