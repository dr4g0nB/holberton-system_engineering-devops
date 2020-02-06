#!/usr/bin/python3
import json
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API.
        If invalid subreddit return 0 otherwise returns the number of subs.
        Return - Number of subscribers for a given subreddit.
    """
    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)

    headers = {
        'User-Agent': 'My User Agent 1.0'
    }

    petit = requests.get(url, headers=headers)
    if petit.status_code == 200:
        petition = petit.json()
        data_subs = petition.get('data')
        subscribers = data_subs.get('subscribers')
        return subscribers
    else:
        return 0
