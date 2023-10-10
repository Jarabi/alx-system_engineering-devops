#!/usr/bin/python3
""" Prints the titles of the first 10 hot
    posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        posts = data["data"]["children"][:10]

        for index, post in enumerate(posts, start=1):
            print(post["data"]["title"])
