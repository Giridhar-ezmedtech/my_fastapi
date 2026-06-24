import pytest
from fastapi.testclient import TestClient
from app import main

# =====================================================================
# test_main.py
# This file contains unit tests for the Employee CRUD endpoints.
# It uses FastAPI's TestClient to simulate HTTP requests.
# Perfect for running in GitHub Actions CI pipeline.
# =====================================================================

client = TestClient(main.app)

@pytest.fixture(autouse=True)
def reset_db():
    """
    Fixture that runs before every test to clear the in-memory database
    and reset the ID counter. This ensures test isolation.
    """
    main.employees_db.clear()
    main.id_counter = 1


def test_read_root():
    """
    Tests GET / to ensure welcome message is correct.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Employee Management API!",
        "docs_url": "/docs"
    }


def test_read_status():
    """
    Tests GET /status to ensure API health status check functions properly.
    """
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "online (in-memory)"
    }



def test_create_employee():
    """
    Tests POST /employees to ensure a new employee can be created.
    """
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@company.com",
        "department": "Engineering",
        "role": "Software Engineer"
    }
    response = client.post("/employees", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@company.com"
    assert data["department"] == "Engineering"
    assert data["role"] == "Software Engineer"


def test_get_employees():
    """
    Tests GET /employees to ensure it returns the list of all employees.
    """
    # Create two employees
    client.post("/employees", json={"name": "Alice", "email": "alice@co.com", "department": "HR", "role": "Recruiter"})
    client.post("/employees", json={"name": "Bob", "email": "bob@co.com", "department": "Sales", "role": "Representative"})
    
    response = client.get("/employees")
    assert response.status_code == 200
    employees = response.json()
    assert len(employees) == 2
    assert employees[0]["name"] == "Alice"
    assert employees[1]["name"] == "Bob"


def test_get_employee_by_id_success():
    """
    Tests GET /employees/{id} for a successful retrieval.
    """
    client.post("/employees", json={"name": "Alice", "email": "alice@co.com", "department": "HR", "role": "Recruiter"})
    
    response = client.get("/employees/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["id"] == 1


def test_get_employee_by_id_not_found():
    """
    Tests GET /employees/{id} returns 404 when the ID does not exist.
    """
    response = client.get("/employees/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee with ID 99 not found."


def test_update_employee_success():
    """
    Tests PUT /employees/{id} updates fields successfully.
    """
    # Create initial employee
    client.post("/employees", json={"name": "Alice", "email": "alice@co.com", "department": "HR", "role": "Recruiter"})
    
    # Partial update: Change role and department
    update_payload = {
        "department": "Engineering",
        "role": "HR Director"
    }
    response = client.put("/employees/1", json=update_payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"  # Unchanged
    assert data["email"] == "alice@co.com"  # Unchanged
    assert data["department"] == "Engineering"  # Updated
    assert data["role"] == "HR Director"  # Updated


def test_update_employee_not_found():
    """
    Tests PUT /employees/{id} returns 404 when updating a non-existent employee.
    """
    update_payload = {"name": "Bob"}
    response = client.put("/employees/99", json=update_payload)
    assert response.status_code == 404


def test_delete_employee_success():
    """
    Tests DELETE /employees/{id} removes the employee.
    """
    client.post("/employees", json={"name": "Alice", "email": "alice@co.com", "department": "HR", "role": "Recruiter"})
    
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]
    
    # Confirm it's gone from database
    get_response = client.get("/employees/1")
    assert get_response.status_code == 404


def test_delete_employee_not_found():
    """
    Tests DELETE /employees/{id} returns 404 when deleting a non-existent employee.
    """
    response = client.delete("/employees/99")
    assert response.status_code == 404
