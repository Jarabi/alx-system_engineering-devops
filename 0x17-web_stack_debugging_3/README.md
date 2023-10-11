# 0x17. Web stack debugging #3

<kbd>DevOps</kbd> &middot; <kbd>SysAdmin</kbd> &middot; <kbd>Scripting</kbd> &middot; <kbd>Debugging</kbd>

## Background Context

Six Stages of Debugging
1. That can't happen.
1. That doesn't happen on my machine.
1. That shouldn't happen.
1. Why does that happen?
1. Oh, I see.
1. How did that ever work?

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… [It actually powers 26% of the web](https://intranet.alxswe.com/rltoken/qxyFYZIwOXQWw02-HaQ7Bw), so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.