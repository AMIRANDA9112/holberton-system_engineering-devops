#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    # Get the user
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user = requests.get(url)
    user = user.json().get('name')

    # Get the task
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos'
    task_li = requests.get(url)
    done = [task for task in task_li.json() if task['completed'] is True]

    ld = len(done)
    lt = len(task_li.json())
    print("Employee {} is done with tasks({}/{}):".format(user, ld, lt))

    for task in done:
        print('\t ' + task['title'])
