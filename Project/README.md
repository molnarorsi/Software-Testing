# Software Testing and Validation Project 2024

## Employee Management System

This project is a simple Employee Management System implemented in Python. It includes functionalities such as calculating employee salary, sending salary notifications and displaying employee information.

### Project Structure
The project has two main directories: `src` and `tests`. The `src` directory contains the source code of the project, while the `tests` directory contains the test cases for the project.

### Installation
To install the necessary dependencies for this project , run the following command:
```bash
pip install -r requirements.txt
```

### Running Tests
To run the test cases for this project, navigate to the project directory and run the following command:
```bash
pytest tests
```

### Modules
**1.Employee:**
This module defines the `Employee` class, which represents an employee in the system. It contains attributes such as `name`, `id`, `salary`, `email`, etc.

**2.EmployeeManager:**
This module defines the `EmployeeManager` class, which is responsible for managing employees and calculating their salaries. It contains methods such as `calculate_salary`, etc.

**3.RelationsManager:**
This module defines the `RelationsManager` class, which is responsible for managing the relationships between employees and their managers. It contains methods such as `is_leader()`, `get_team_members()`, etc.