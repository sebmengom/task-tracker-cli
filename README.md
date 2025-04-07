# 📝 Task Tracker CLI  
A simple and efficient command-line application to manage your tasks with support for statuses, descriptions, and timestamps.  
https://roadmap.sh/projects/task-tracker

## 🚀 Features  
- ✅ Add tasks with title, description, and status  
- ✏️ Update task descriptions  
- 🔄 Mark tasks as **In Progress** or **Done**  
- ❌ Delete tasks  
- 📋 List all tasks  
- 🔍 Filter tasks by status: `TODO`, `IN PROGRESS`, or `DONE`  

## 🛠 Installation  
1. Make sure you have **Python 3.x** installed.  
2. Clone the repository:  
   `git clone <https://github.com/sebmengom/task-tracker-cli> & cd task-tracker-cli`  

## ⚙️ Usage  
### ➕ Add a Task  
`python3 task_cli.py add "Task Title"`  
`python3 task_cli.py add "Task Title" --description "Task description"`  
`python3 task_cli.py add "Task Title" --status "IN PROGRESS"`  

### 📝 Update a Task  
`python3 task_cli.py update <task_id> "New description"`  

### 🔄 Change Task Status  
`python3 task_cli.py mark-in-progress <task_id>`  
`python3 task_cli.py mark-done <task_id>`  

### 🗑 Delete a Task  
`python3 task_cli.py delete <task_id>`  

### 📋 List Tasks  
`python3 task_cli.py list`  
`python3 task_cli.py list-todo`  
`python3 task_cli.py list-in-progress`  
`python3 task_cli.py list-done`  

## 🗂 Task Status Options  
- `TODO` (default)  
- `IN PROGRESS`  
- `DONE`  

## 💾 File Storage  
Tasks are stored in a `tasks.json` file located in the same directory as the script. This file is created automatically when you add your first task.  

## 📄 Task Properties  
Each task includes the following properties:  
- `ID`: Automatically assigned  
- `Title`: Required  
- `Description`: Optional  
- `Status`: Default is `TODO`  
- `Created`: Timestamp of creation  
- `Updated`: Timestamp of last update
