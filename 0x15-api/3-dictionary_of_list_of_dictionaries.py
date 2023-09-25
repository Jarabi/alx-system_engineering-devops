#!/usr/bin/python3
""" A Python script that exports data in JSON foramt """


def export_to_json(emp_data, task_data):
    """
    Export data to JSON

    Args:
        emp_data: Employee data
        task_data: Employee tasks
    """

    json_file = "todo_all_employees.json"
    all_tasks = {}

    # Extract user id and username
    for user in emp_data:
        user_tasks = []
        user_id = user['id']
        username = user['username']

        my_tasks = [task for task in task_data if task['userId'] == user_id]

        # Extract task data for user
        for my_task in my_tasks:
            user_tasks.append({
                "username": username,
                "task": my_task['title'],
                "completed": my_task['completed']})

        all_tasks.update({f"{user_id}": user_tasks})

    # Dump to JSON file
    with open(json_file, mode='w') as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    import json
    import requests

    user_api_url = "https://jsonplaceholder.typicode.com/users/"
    todo_api_url = "https://jsonplaceholder.typicode.com/todos/"

    # Get all employee details
    employee_data = requests.get(user_api_url).json()

    # Get all tasks
    todo_data = requests.get(todo_api_url).json()

    # Export to JSON
    export_to_json(employee_data, todo_data)
