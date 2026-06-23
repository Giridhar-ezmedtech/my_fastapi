# FastAPI Employee CRUD Application

This is a simple, beginner-friendly Employee CRUD application built using Python and **FastAPI**. It is designed specifically for learning how to deploy applications using CI/CD pipelines (e.g., GitHub Actions).

## Features
- **FastAPI Framework**: High performance, easy to learn, fast to code.
- **Pydantic Models**: Automatic request validation and response serialization.
- **In-Memory Data Store**: Simulates a database using a simple Python list. No database installation is required!
- **Unit Tests**: Full suite of unit tests with `pytest` ready to be integrated into any CI/CD pipeline.
- **Auto-generated Documentation**: Interactive API documentation at `/docs` (Swagger UI).

---

## File Structure

```text
Curd-fastapi/
├── app/
│   ├── __init__.py       # Makes 'app' a importable package
│   ├── main.py           # Application entrypoint & route implementations
│   └── schemas.py        # Pydantic models for data validation
├── tests/
│   ├── __init__.py       # Makes 'tests' a importable package
│   └── test_main.py      # Unit tests for the CRUD API
├── requirements.txt      # Project dependencies (FastAPI, Pytest, etc.)
└── README.md             # This setup and documentation file
```

---

## File Explanations

1. **`app/schemas.py`**: Contains the Pydantic models (data schemas) which declare what the request body and response payload structure should look like. FastAPI uses these to perform automatic input validation and generate Swagger schemas.
2. **`app/main.py`**: Initializes the FastAPI application, sets up the in-memory employee list database, and defines all path operations (endpoints) for the welcome message, creating, reading, updating, and deleting employees.
3. **`tests/test_main.py`**: Uses FastAPI's built-in `TestClient` and `pytest` to verify that all API endpoints function correctly. The database is cleared before each test runs to ensure test isolation.
4. **`requirements.txt`**: Lists all libraries/dependencies needed to run and test the application.

---

## How to Run the Application Locally

Follow these step-by-step instructions to get the application running on your local machine:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. You can verify your Python installation by running:
```bash
python --version
```

### 2. Create a Virtual Environment (Recommended)
Creating a virtual environment ensures that the dependencies for this project don't conflict with other Python projects on your machine.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all the required Python packages specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Start the Application
Run the application using the **Uvicorn** development server:
```bash
uvicorn app.main:app --reload
```
- `app.main:app` refers to the `app` instance in `app/main.py`.
- `--reload` enables auto-reloading, which means the server will automatically restart whenever you make changes to the code.

You should see output indicating that the server is running, usually at `http://127.0.0.1:8000`.

### 5. Access the Interactive API Documentation
FastAPI automatically generates interactive Swagger documentation for the endpoints.
- Open your web browser and navigate to: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
- From here, you can click on any endpoint, click "Try it out", fill in parameters, and click "Execute" to make live requests to your running app.

---

## How to Run Tests Locally

Before pushing changes to GitHub, it is good practice to run tests locally to ensure nothing is broken. This also matches what the CI/CD pipeline runs.

With your virtual environment active, run:
```bash
pytest
```

Pytest will automatically scan the `tests/` directory, execute all tests prefixed with `test_`, and output the results.
