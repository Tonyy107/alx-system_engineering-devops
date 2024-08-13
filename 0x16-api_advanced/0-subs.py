#!/usr/bin/python3
"""0-subs"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit. Returns 0
        if the request fails or the subreddit does not exist.
    """

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "tony"},
        allow_redirects=False
    )

    if req.status_code == 200:
        return req.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
