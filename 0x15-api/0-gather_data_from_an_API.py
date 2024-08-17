#!/usr/bin/python3
""" api hoho """
import requests
import sys

if __name__ == "__main__":

    # استرجاع معلومات المستخدم باستخدام المعرف المدخل
    url = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
    ids = url.json()
    name = ids["name"]

    # استرجاع المهام الخاصة بالمستخدم
    url2 = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}")
    tasks = url2.json()

    # تصفية المهام المكتملة
    com = []
    for task in tasks:
        if task["completed"]:
            com.append(task)

    # طباعة الإخراج المطلوب
    print(f"Employee {name} is done with tasks({len(com)}/{len(tasks)}):")

    for task in com:
        task_title = task["title"]
        print(f"\t {task_title}")
