# Tasks Manager and Tracker

A Python-based application for managing tasks efficiently. This tool allows users to add, update, delete, filter, and sort tasks based on various attributes like due dates, priority levels, and status. Designed for flexibility and scalability, this project is perfect for personal task management or small teams.

## Features

- **Add Tasks:** Create new tasks with attributes such as name, category, due date, priority, and status.
- **Update Tasks:** Modify existing task details.
- **Delete Tasks:** Remove tasks from the list.
- **Filter Tasks:** View tasks filtered by attributes like priority or status.
- **Sort Tasks:** Organize tasks by due date, priority, status or name.
- **Enum Integration:** Use `Priority` ans `Status` enums for streamlined task management.
- **Error Handling:** Handles invalid inputs gracefully with meaningful error messages.

## Installation

Follow these steps to set up and run the project:
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/vicuartas230/tasks_manager_and_tracker.git
    cd tasks_manager_and_tracker
    ```
2. **Set Up a Virtual Environment:**
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. **Run Tests:** Ensure everything is working as expected:
    ```bash
    python -m unittest discover tests/
    ```
4. **Run the Application:**
    ``` bash
    python3 main.py
    ```

## Usage
### Adding a Task
```python
python3 main.py add "Task 1" "Personal" "2024-11-30" "High" "Pending"
```

### Updating a Task
```python
python3 main.py update <task_id> --status "In-progress"
```

### Listing all tasks
```python
python3 main.py view
```

### Sorting Tasks
```python
python3 main.py sort --name --reverse
```

### Filtering Tasks
```python
python3 main.py filter --status "Pending"
```

### Deleting a Task
```python
python3 main.py delete <task_id>
```

## Testing
All core functionalities are covered with `uniitest`. To run the rest suite:
```bash
python -m unittest discover tests/
```

Sample test case:
```python
def test_add_task(self):
    self.manager.add_task("Test Task", "General", "2024-11-20", "Medium", "Pending")
    self.assertEqual(len(self.manager.all_tasks()), 1)
```

## Directory Structure

```
tasks_manager_and_tracker/
├── tasks/
│   ├── task_manager.py      # Core functionality for task management
│   └── task.py              # Task class implementation
├── tests/
│   ├── test_task_manager.py # Unit tests for TaskManager
│   └── test_task.py         # Unit tests for Task class
├── utils/
│   └── enums.py             # Enum definitions for Priority and Status
├── main.py                  # CLI interface
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Dependencies
This project uses the following Python packages:
- `pytest` (optional for additional testing)
- Add any other dependencies you've used.

Install them via:
```bash
pip install -r requirements.txt
```
