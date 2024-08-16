#!/usr/bin/python3
"""hi"""
import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit. Returns 0
        if the request fails, the subreddit does not exist, or a redirect occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "myapp/0.0.1 (by u/yourusername)"}

    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        print(req.status_code)  # Debug: Check status code
        print(req.text)         # Debug: Check response content
        
        if req.status_code == 200:
            return req.json().get("data", {}).get("subscribers", 0)
        elif req.status_code in (302, 404):
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0
