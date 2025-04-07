#Import libraries
import argparse
import json
import os
from datetime import datetime

#File to store tasks
TASKS_F = "tasks.json" 

def load_tasks():
    if os.path.exists(TASKS_F): #Open File if it exists
        with open (TASKS_F, 'r') as f:
            return json.load(f)
    return [] #Create file if it doesnt exist

def save_tasks(tasks):
    with open(TASKS_F, 'w') as f: #Save JSON file with proper formatting
        json.dump(tasks, f, indent=2)

def format_task(task): #Formatting of a single tasks
    output=[
        ('Task\n----------'),
    f'ID:{task['id']}',
    f'Title:{task['title']}',
    f'Status:{task['status']}',
    ]
    if task.get('description'):
        output.append(f'Description:{task['description']}')
    output.extend([
        f'Created on:{task['created_at']}',
        f'Last updated on:{task['last_updated']}',
              '----------'
    ])
    print( '\n'.join(output))
def format_lists(tasks): #Format of a list of tasks
    print('Found Tasks\n----------')
    for task in tasks:
        print(f'ID:{task['id']}')
        print(f'Title:{task['title']}')
        print(f'Status:{task['status']}')
        if task.get('description'):
            print(f'Description:{task['description']}')
        print(f'Created on:{task['created_at']}')
        print(f'Last updated on:{task['last_updated']}')
        print('----------')
    
def add_tasks(args): #ADD a  new task, args are the command line arguments
    tasks = load_tasks()
    new_task = {
        'id': len(tasks)+1,
        'title':args.title,
        'description':args.description,
        'status':args.status,
        'created_at': datetime.now().isoformat(),
        'last_updated': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    format_task(new_task)
    print(f'Task {new_task['id']} added!')

def update_task(args): #Update task using the task id, args are the command line arguments
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.task_id:
            task['description'] = args.new_description
            task['last_updated'] = datetime.now().isoformat()
            save_tasks(tasks)
            format_task(task)
            print('Task updated!')
            return
    print('Task not found')

def delete_task(args): #delete tasks using the task id, args are the command line arguments
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.task_id:
            for t in tasks[args.task_id:]:
                t['id'] -= 1
            tasks.remove(task)
            save_tasks(tasks)
            print('Task Removed')
            return
    print('Task not found')

def in_progress(args): #mark task as in progress using the task id, args are the command line arguments
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.task_id:
            task['status'] = "IN PROGRESS"
            task['last_updated']= datetime.now().isoformat()
            save_tasks(tasks)
            format_task(task)
            print('Marked in progress')
            return
    print('Task not found')

def done (args): #mark task as done using the task id, args are the command line arguments
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.task_id:
            task['status'] = "DONE"
            task['last_updated'] = datetime.now().isoformat()
            save_tasks(tasks)
            format_task(task)
            print('YOU FINISHED YOUR TASK!! 🎉')
            return
    print('Task not found')
        
def listing(args):  #print list of all tasks
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    format_lists(tasks)

def list_todo(args): #print list of TODO tasks
    tasks = load_tasks()
    todo_tasks = []
    for t in tasks:
        if t['status'] == "TODO":
            todo_tasks.append(t)
    if not todo_tasks:
        print('No TODO tasks found!')
        return
    format_lists(todo_tasks)

def list_IP(args): #print list of in-progress tasks
    tasks = load_tasks()
    ip_tasks = []
    for t in tasks:
        if t['status'] == "IN PROGRESS":
            ip_tasks.append(t)
    if not ip_tasks:
        print('No IN PROGRESS tasks found!')
        return
    format_lists(ip_tasks)

def list_done(args): #print list of done tasks
    tasks = load_tasks()
    done_tasks = []
    for t in tasks:
        if t['status'] == "DONE":
            done_tasks.append(t)
    if not done_tasks:
        print('No DONE tasks found!')
        return
    format_lists(done_tasks)

if __name__ == "__main__":
    #setup command line arguments parse
    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    #Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('--description', help='Task description')
    add_parser.add_argument('--status', default='TODO', help='Task status')
    #Update task command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('task_id', type=int, help='Task ID to update')
    update_parser.add_argument('new_description')
    #In progress command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
    mark_in_progress_parser.add_argument('task_id', type = int)
    #Done command
    done_parser = subparsers.add_parser('mark-done')
    done_parser.add_argument('task_id', type=int)
    #Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', type=int, help='Task ID to delete')
    #Lists command
    list_parser = subparsers.add_parser('list')
    todo_list_parser = subparsers.add_parser('list-todo')
    in_progress_list_parser = subparsers.add_parser('list-in-progress')
    done_list_parser = subparsers.add_parser('list-done')

    #parse the arguments and execute.
    args = parser.parse_args()

    if args.command == 'add':
        add_tasks(args)
    elif args.command == 'update':
        update_task(args)
    elif args.command == 'delete':
        delete_task(args)
    elif args.command == 'mark-in-progress': 
        in_progress(args)
    elif args.command == 'mark-done': 
        done(args)
    elif args.command == 'list':
        listing(args)
    elif args.command == 'list-todo':
        list_todo(args)
    elif args.command == 'list-in-progress':
        list_IP(args)
    elif args.command == 'list-done':
        list_done(args)