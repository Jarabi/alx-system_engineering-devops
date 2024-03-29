#!/usr/bin/python3
""" A Python script that exports data in CSV foramt """


if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    employee_id = argv[1]
    baseurl = "https://jsonplaceholder.typicode.com"
    employee_api_url = f"{baseurl}/users/{employee_id}"
    todo_api_url = f"{baseurl}/todos?userId={employee_id}"
    filename = f"{employee_id}.csv"

    # Get employee details
    employee_data = requests.get(employee_api_url)
    username = employee_data.json()["username"]

    # Get tasks for employee
    todo_data = requests.get(todo_api_url).json()

    with open(filename, mode='w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            completed = task['completed']
            title = task['title']
            writer.writerow([employee_id, username, completed, title])
