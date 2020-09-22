#!/usr/bin/python3
""" Returns the number of subscribers for a given subreddit """

import requests


def number_of_subscribers(subreddit):
    """Qeries Reddit API"""
    header = {"User-Agent": "My-User-Agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    query = requests.get(url, headers=header, allow_redirects=False)

    if query.status_code >= 300:
        return 0

    return query.json().get('data', {}).get('subscribers', 0)
