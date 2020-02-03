#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[2]
    """ Information from json placeholder converted in json format """
    ph_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    ph_todos = request.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)).json()
    """ Empty list to fill in with the todos list """
    all_tasks = []
    """  Traversing the todos list """
    for looking_tasks in ph_todos:
        """ Filtering the list to obtain the completed value """
        if looking_tasks.get("completed"):
            """ Appending the content of the dict to the empty list """
            all_tasks.append(looking_tasks.get("title"))
    """ Printing the dictionary """
    print("Employee {} is done with tasks({}/{}):".format(ph_users.get("name"), len(all_tasks), len(ph_todos)))
    # Filtering down to only show the tasks 
    for looking_tasks in all_tasks:
        print("\t {}".format(looking_tasks))