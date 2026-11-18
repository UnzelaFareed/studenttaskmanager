
# Student Task Manager - User Guide

## 1. Introduction
Student Task Manager is a simple Python console application used to manage daily tasks.

## 2. Requirements
- Python 3 installed
- Git installed (for cloning the project)

## 3. Setup
1. Clone the repository:
   `git clone https://github.com/UnzelaFareed/studenttaskmanager.git`
2. Open the project folder:
   `cd studenttaskmanager`
3. Run the application:
   `python main.py`

## 4. Available Operations
- Add Task: Enter a task title to create a new task.
- Display Tasks: View all tasks and their IDs and status.
- Complete Task: Enter a task ID to mark it as completed.
- Delete Task: Enter a task ID to delete a task.

## 5. Input Validation
- Empty task titles are not accepted.
- Enter a valid task ID when completing or deleting a task.
- Invalid menu choices are handled by the application.

## 6. Running Unit Tests
Run this command in the project directory:

`python -m unittest discover -s tests -v`

The tests check adding, completing, and deleting tasks.
