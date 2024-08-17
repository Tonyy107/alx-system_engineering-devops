#!/usr/bin/python3
""" API Output Checker """
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_resp = requests.get(user_url).json()
    todos_resp = requests.get(todos_url).json()

    name = user_resp["name"]

    completed_tasks = [task["title"]
                       for task in todos_resp if task["completed"]]
    total_tasks = len(todos_resp)

    print(f"Employee {name} is done with tasks\
({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task}")
