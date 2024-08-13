# api_advanced

## Tasks

### 0. How many subs?

**Task:**  
Write a Python function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is provided, the function should return `0`.

**Function Signature:**
```py
def number_of_subscribers(subreddit):
    pass
```
### 1. Top Ten

**Task:**
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Function Signature:**
```py
def top_ten(subreddit):
```
### 2. Recurse it!

**Task:**
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

**Function Signature:**
```py
def recurse(subreddit, hot_list=[]):
```