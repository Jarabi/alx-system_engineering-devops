#!/usr/bin/python3
""" Prints the titles of the first 10 hot
    posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of
    the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    res = requests.get(url, headers=headers)

    data = res.json()
    posts = data.get('data', {}).get('children', None)

    if posts is None:
        print(posts)
    else:
        for post in posts:
            print(post["data"]["title"])
