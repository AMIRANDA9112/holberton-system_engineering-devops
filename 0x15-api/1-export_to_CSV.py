#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script
to export data in the CSV format .
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    r_user = requests.get(url_user)
    r_todos = requests.get(url_todos)
    json_user = r_user.json()
    json_todos = r_todos.json()
    employee_username = json_user['username']

    with open(user_id + '.csv', mode='w') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in json_todos:
            writer.writerow([user_id, employee_username,
                            task['completed'], task['title']])
