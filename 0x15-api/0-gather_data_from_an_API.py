#!/usr/bin/python3
""" api hoho """
import requests
import sys


if __name__ == "__main__":

    url = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    ids = url.json()
    print(f"Employee {ids.get('name')} is done with tasks", end="")
    url2 = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}")
    tasks = url2.json()
    com = []
    for task in tasks:

        if task.get("completed") is True:
            com.append(task)
    print(f"({len(com)}/{len(tasks)}):")

    for task in com:
        task = task.get("title")
        print(f"\t{task}")
