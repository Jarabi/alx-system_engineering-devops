# 0x16. API advanced

<kbd>Python</kbd> &middot; <kbd>Scripting</kbd> &middot; <kbd>Back-end</kbd> &middot; <kbd>API</kbd>

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

<small>Script: [0-subs.py](https://github.com/Jarabi/alx-system_engineering-devops/blob/main/0x16-api_advanced/0-subs.py)</small>

A function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

### 1. Top Ten

<small>Script: [1-top_ten.py](https://github.com/Jarabi/alx-system_engineering-devops/blob/main/0x16-api_advanced/1-top_ten.py)</small>

A function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and prints the titles of the first 10 hot posts listed for a given subreddit. If not a valid subreddit, the function prints None.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
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

### 2. Recurse it!

<small>Script: [2-recurse.py](https://github.com/Jarabi/alx-system_engineering-devops/blob/main/0x16-api_advanced/2-recurse.py)</small>

A recursive function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

> [!NOTE]
> Invalid subreddits may return a redirect to search results. Script does not follow redirects.

```bash
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
```

### 3. Count it!
<small>Script: [2-recurse.py](https://github.com/Jarabi/alx-system_engineering-devops/blob/main/0x16-api_advanced/2-recurse.py)</small>

A recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords. If no posts match or the subreddit is invalid, it prints nothing.

Results are printed in descending order, by the count, and if the count is the same for separate keywords, they are then sorted alphabetically (A to Z). Words with no matches are skipped and not printed. Words are printed in lowercase.

```bash
$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
$ python3 100-main.py programming 'JavA java'
java: 54
$ python3 100-main.py not_a_valid_subreddit 'python java javascript scala no_results_for_this_one'
$ python3 100-main.py not_a_valid_subreddit 'python java'
$
```
