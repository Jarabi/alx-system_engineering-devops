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

## Tasks

### 0. Strace is your friend

<small>Script: [0-strace_is_your_friend.pp](https://github.com/Jarabi/alx-system_engineering-devops/blob/main/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)</small>

The tool [strace](https://intranet.alxswe.com/rltoken/ueMevAif95DjyW2sqVCMoA) is used to find out why Apache is returning a 500 error. Once the issue is discovered, the fix is then automated using Puppet (instead of using Bash). `strace` is handy because it attaches to a running process and is useful for diagnosis.

In this task, we use [tmux](https://intranet.alxswe.com/rltoken/UsSRoxIYdq0l0QUIuDNnSw) to run `strace` in one terminal, and `curl` in another (not tmux).

#### tmux installation and use

On Ubuntu, WSL:
```bash
$ sudo apt-get install tmux
```

On Mac:
```bash
$ brew install tmux
```

Start session:
```bash
$ tmux
```

This will create a new tmux session with a nice <span style="color: #4e9a06;">all-green status bar</span> at the bottom.

Next, within tmux, find the PID of the Apache process:

```bash
# ps aux | grep apache
root        91  0.0  0.1 276396 21708 ?        Ss   17:58   0:00 /usr/sbin/apache2 -k start
www-data   134  0.0  0.2 280520 35480 ?        S    17:58   0:00 /usr/sbin/apache2 -k start
www-data   768  0.0  0.2 284384 44820 ?        S    22:02   0:00 /usr/sbin/apache2 -k start
root      3469  0.0  0.0   8864   812 pts/6    S+   23:55   0:00 grep --color=auto apache
```

Next, attach `strace` to the Apache PID (still in the tmux session):

```bash
# strace -f -p 768
Process 768 attached
accept4(3, 
```

In another terminal, simulate the issue with `curl`:

```bash
# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
```
You can see that the simulation causes an internal server err (500). In the `tmux` window, a sample of the output is displayed below. Note the 'No such file or directory' reference to the file "/var/www/html/wp-includes/class-wp.phpp"
```bash
...
lstat("/var/www/html/wp-includes/class-wp.phpp", 0x7fff0101e410) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp.phpp", 0x7fff01020640) = -1 ENOENT (No such file or directory)
open("/var/www/html/wp-includes/class-wp.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
...
read(4, 0x7fff010259d7, 1)              = -1 EAGAIN (Resource temporarily unavailable)
accept4(3, 
```
This points to a misconfiguration that is looking for a non-standard '.phpp' file. A quick check at some of the WordPress core files (which normally access `class-wp-locale.php`) reveals that the misconfiguration is within the file `/var/www/html/wp-settings.php`.

#### Automate the solution

The puppet file is run to resolve the error and the server is now  up and running:

```bash
# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
#
# curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8
#
# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
#
```