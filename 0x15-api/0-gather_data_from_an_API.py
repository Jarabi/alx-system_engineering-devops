#!/usr/bin/python3
""" A Python script that uses REST API for a given employee ID
and returns information about his/her TODO list progress. """


if __name__ == "__main__":
    import requests
    from sys import argv

    emp_id = argv[1]
    emp_api_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    # Get employee data
    emp_data = requests.get(emp_api_url)
    emp_name = emp_data.json()["name"]

    # Get tasks for employee
    todo_data = requests.get(todo_url)
    todo_list = todo_data.json()
    completed = [task for task in todo_list if task['completed']]

    # Task statistics
    total = len(todo_list)
    done = len(completed)

    print(f"Employee {emp_name} is done with tasks({done}/{total}):")

    for task in completed:
        print(f"\t {task['title']}")
