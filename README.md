# FastAPI Employee CRUD Application

This is a simple, beginner-friendly Employee CRUD application built using Python and **FastAPI**. It is designed specifically for learning how to deploy applications using CI/CD pipelines (e.g., GitHub Actions).

This repository is optimized to use **Astral `uv`**, a fast Python package manager and resolver that handles virtual environment creation and package installation automatically.

## Features
- **FastAPI Framework**: High performance, easy to learn, fast to code.
- **Pydantic Models**: Automatic request validation and response serialization.
- **In-Memory Data Store**: Simulates a database using a simple Python list. No database installation is required!
- **Unit Tests**: Full suite of unit tests with `pytest` ready to be integrated into any CI/CD pipeline.
- **Auto-generated Documentation**: Interactive API documentation at `/docs` (Swagger UI).
- **Astral `uv`**: Modern package management using a consolidated environment.

---

## File Structure

```text
Curd-fastapi/
├── app/
│   ├── __init__.py       # Makes 'app' an importable package
│   ├── main.py           # Application entrypoint & route operations
│   └── schemas.py        # Pydantic models for data validation
├── tests/
│   ├── __init__.py       # Makes 'tests' an importable package
│   └── test_main.py      # Unit tests for the CRUD API
├── pyproject.toml        # Astral uv configuration, project setup & dependencies
├── requirements.txt      # Backup pip dependency list
└── README.md             # This setup and documentation file
```

---

## File Explanations

1. **`app/schemas.py`**: Contains the Pydantic models (data schemas) which declare what the request body and response payload structure should look like. FastAPI uses these to perform automatic input validation and generate Swagger schemas.
2. **`app/main.py`**: Initializes the FastAPI application, sets up the in-memory employee list database, and defines all path operations (endpoints) for the welcome message, creating, reading, updating, and deleting employees.
3. **`tests/test_main.py`**: Uses FastAPI's built-in `TestClient` and `pytest` to verify that all API endpoints function correctly. The database is cleared before each test runs to ensure test isolation.
4. **`pyproject.toml`**: The modern configuration file for your Python workspace. Specifies metadata and lists packages (under `dependencies` and `dependency-groups`) managed by Astral `uv`.

---

## How to Run the Application Locally (Using `uv`)

Follow these step-by-step instructions to get the application running on your local machine using the Astral `uv` tool:

### 1. Install `uv`
If you haven't installed `uv` yet, you can install it using:

*   **Windows (PowerShell):**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
*   **macOS / Linux:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

Verify your installation:
```bash
uv --version
```

### 2. Setup the Environment & Install Dependencies
Run the sync command inside the project directory. `uv` will automatically discover your Python version, create a local `.venv` folder, and install all dependencies:
```bash
uv sync
```

### 3. Start the Application
Run the application using `uv run`. This automatically executes the command inside the virtual environment without needing manual activation:
```bash
uv run uvicorn app.main:app --reload
```
- `app.main:app` refers to the `app` instance in `app/main.py`.
- `--reload` enables auto-reloading, which means the server will automatically restart whenever you make changes to the code.

You should see output indicating that the server is running at `http://127.0.0.1:8000`.

### 4. Access the Interactive API Documentation
FastAPI automatically generates interactive Swagger documentation for the endpoints.
- Open your web browser and navigate to: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
- From here, you can click on any endpoint, click "Try it out", fill in parameters, and click "Execute" to make live requests to your running app.

---

## How to Run Tests Locally (Using `uv`)

Before pushing changes to GitHub, it is good practice to run tests locally to ensure nothing is broken. This also matches what the CI/CD pipeline runs.

Execute the test suite using `uv run`:
```bash
uv run pytest
```

`pytest` will automatically scan the `tests/` directory, execute all tests prefixed with `test_`, and output the results.
