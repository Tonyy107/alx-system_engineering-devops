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

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "api_advanced (by /u/bdov_)"}

    try:

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:

            return response.json().get("data", {}).get("subscribers", 0)
        elif response.status_code in (302, 404):

            return 0
        else:
            return 0
    except requests.RequestException:
        return 0
