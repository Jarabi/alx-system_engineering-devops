#!/usr/bin/python3
""" A Python script that exports data in CSV foramt """


def export_to_json(emp_id, username, data):
    """
    Export data to JSON

    Args:
        emp_id: Id of employee
        username: Employee's username
        data: Dictionary of user task details
    """

    json_file = f"{emp_id}.json"
    tasks = []

    # Extract the reuired task details
    for task in data:
        title = task['title']
        completed = task['completed']

        tasks.append({
            "task": title,
            "completed": completed,
            "username": username})

    employee_tasks = {f"{employee_id}": tasks}

    # Dump to JSON file
    with open(json_file, mode='w') as f:
        json.dump(employee_tasks, f)


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_id = argv[1]
    baseurl = "https://jsonplaceholder.typicode.com"
    employee_api_url = f"{baseurl}/users/{employee_id}"
    todo_api_url = f"{baseurl}/todos?userId={employee_id}"

    # Get employee details
    employee_data = requests.get(employee_api_url)
    username = employee_data.json()["username"]

    # Get tasks for employee
    todo_data = requests.get(todo_api_url).json()

    # Export to JSON
    export_to_json(employee_id, username, todo_data)
