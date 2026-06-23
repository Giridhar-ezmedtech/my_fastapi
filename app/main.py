from fastapi import FastAPI, HTTPException, status
from typing import List
from app.schemas import Employee, EmployeeCreate, EmployeeUpdate

# =====================================================================
# main.py
# This is the main entry point of the FastAPI application.
# It initializes the FastAPI app, manages the in-memory database,
# and defines the CRUD endpoints.
# =====================================================================

app = FastAPI(
    title="Employee Management API",
    description="A simple FastAPI CRUD application for learning CI/CD deployment using GitHub Actions.",
    version="1.0.0"
)

# In-memory "database" storing employee records as dictionaries
employees_db = []

# Counter to generate unique IDs for new employees
id_counter = 1

# 1. GET / - Welcome endpoint
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    """
    Returns a simple welcome message. Perfect for testing if the service is up.
    """
    return {
        "message": "Welcome to the Employee Management API!",
        "docs_url": "/docs"
    }

# 2. POST /employees - Create a new employee
@app.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate):
    """
    Creates a new employee record and appends it to the in-memory database.
    Generates a unique ID automatically.
    """
    global id_counter
    # Convert Pydantic model to Python dictionary
    employee_data = employee.model_dump()
    
    # Assign a unique ID
    employee_data["id"] = id_counter
    id_counter += 1
    
    # Save the employee and return the saved data
    employees_db.append(employee_data)
    return employee_data

# 3. GET /employees - Get all employees
@app.get("/employees", response_model=List[Employee], status_code=status.HTTP_200_OK)
def get_employees():
    """
    Retrieves all employee records from the in-memory database.
    """
    return employees_db

# 4. GET /employees/{employee_id} - Get a single employee
@app.get("/employees/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def get_employee(employee_id: int):
    """
    Retrieves a single employee by their unique ID.
    Raises an HTTP 404 error if the employee is not found.
    """
    for emp in employees_db:
        if emp["id"] == employee_id:
            return emp
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee with ID {employee_id} not found."
    )

# 5. PUT /employees/{employee_id} - Update an employee
@app.put("/employees/{employee_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def update_employee(employee_id: int, employee_update: EmployeeUpdate):
    """
    Updates fields of an existing employee by their ID.
    Only updates fields that are explicitly provided in the request payload.
    Raises an HTTP 404 error if the employee is not found.
    """
    for emp in employees_db:
        if emp["id"] == employee_id:
            # Get updated fields (filtering out fields that were not provided)
            update_data = employee_update.model_dump(exclude_unset=True)
            for key, val in update_data.items():
                emp[key] = val
            return emp
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee with ID {employee_id} not found."
    )

# 6. DELETE /employees/{employee_id} - Delete an employee
@app.delete("/employees/{employee_id}", status_code=status.HTTP_200_OK)
def delete_employee(employee_id: int):
    """
    Deletes an employee from the in-memory database by their ID.
    Raises an HTTP 404 error if the employee is not found.
    """
    for index, emp in enumerate(employees_db):
        if emp["id"] == employee_id:
            deleted_emp = employees_db.pop(index)
            return {"message": f"Employee '{deleted_emp['name']}' with ID {employee_id} was successfully deleted."}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee with ID {employee_id} not found."
    )
