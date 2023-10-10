#!/usr/bin/python3
""" Prints a sorted count of given keywords """
import requests
after = None


def count_words(subreddit, word_list = []):
    """ Recursively queries the Reddit API, parses the title of all
        hot articles, and prints a sorted count of given keywords
        (case-insensitive, delimited by spaces) """
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
        word_list.append(title)

    after = data.get('after')

    if after is None:
        return word_list

    return count_words(subreddit, word_list)
