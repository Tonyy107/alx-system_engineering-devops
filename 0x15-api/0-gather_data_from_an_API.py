#!/usr/bin/python3
""" api hoho """
import requests
import sys


if __name__ == "__main__":

    url = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    ids = url.json()
    print("Employee {} is done with tasks".format(ids.get('name')), end="")
    url2 = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}")
    tasks = url2.json()
    com = []
    for task in tasks:

        if task["completed"] is True:
            com.append(task)
    print("({}/{}):".format(len(com), len(tasks)))

    for task in com:
        print("\t {}".format(task.get("title")))
