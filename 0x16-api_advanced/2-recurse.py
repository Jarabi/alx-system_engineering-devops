#!/usr/bin/python3
""" Returns a list containing the titles of all
    hot articles for a given subreddit """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ Recursively queries the Reddit API and
        returns a list containing the titles of
        all hot articles for a given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'alex-jarabi'}
    global after
    params = {'after': after}

    res = requests.get(url, headers=headers, params=params)
    data = res.json().get('data', {})
    posts = data.get('children', None)

    if posts is None:
        return None

    for post in posts:
        title = post.get('data', {}).get('title')
        hot_list.append(title)

    after = data.get('after')

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)
