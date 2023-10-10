#!/usr/bin/python3
import requests
""" Returns the number of
    subscribers for a given subreddit """


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    res = requests.get(url, headers=headers)
    subs = 0

    if res.status_code == 200:
        data = res.json()
        subs = data["data"]["subscribers"]

    return subs
