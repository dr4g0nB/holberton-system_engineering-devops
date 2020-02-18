#!/usr/bin/python3
import json
import requests


def top_ten(subreddit):
    """
        Queries the Reddit API .
        Prints the titles of the first 10 hot posts listed for subreddit
        or prints None.
    """
    url = 'https://api.reddit.com/r/{}?sort=hot&limit=10'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    petit = requests.get(url, headers=headers)
    if petit.status_code == 200:
        petition = petit.json()
        data_subs = petition.get('data')
        data_child = data_subs.get('children')
        for trav in data_child:
            traversed_list = trav.get('data').get('title')
            print(traversed_list)
    else:
        print(None)
