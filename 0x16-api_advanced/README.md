# 0x16. API advanced

<kbd>Python</kbd> &middot; <kbd>Scripting</kbd> &middot; <kbd>Back-end</kbd> &middot; <kbd>API<kbd>

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA). There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Learning Objectives
* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

## Tasks

### 0. How many subscribers?

A function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
$
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

> Script: 0-subs.py

### 1. Top Ten

A function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and prints the titles of the first 10 hot posts listed for a given subreddit. If not a valid subreddit, the function prints None.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
$ cat 1-main.py
#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
$
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
$
$ python3 1-main.py this_is_a_fake_subreddit
None
$ 
```

> Script: 1-top_ten.py

### 2. Recurse it!

A recursive function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
$ cat 2-main.py
#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
$
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

> Script: 2-recurse.py