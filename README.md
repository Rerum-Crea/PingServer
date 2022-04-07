
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![GitHub issues](https://img.shields.io/github/issues/Necrownyx/PingServer)](https://github.com/Necrownyx/PingServer/issues) [![GitHub forks](https://img.shields.io/github/forks/Necrownyx/PingServer)](https://github.com/Necrownyx/PingServer/network) [![GitHub stars](https://img.shields.io/github/stars/Necrownyx/PingServer)](https://github.com/Necrownyx/PingServer/stargazers) [![GitHub license](https://img.shields.io/github/license/Necrownyx/PingServer)](https://github.com/Necrownyx/PingServer/blob/main/LICENSE) [![Python](https://img.shields.io/badge/Made%20with-Python-%2300AEFF)](https://python.org) [![Python](https://img.shields.io/badge/Available%20on-PyPi-%2300AEFF)](https://pypi.org/project/PingServer/) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FNecrownyx%2FPingServer&count_bg=%2300AEFF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If you like the package please can you star the github.


<pre align="center">██████╗ ██╗███╗   ██╗ ██████╗     ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██║████╗  ██║██╔════╝     ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██████╔╝██║██╔██╗ ██║██║  ███╗    ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██╔═══╝ ██║██║╚██╗██║██║   ██║    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║╚██████╔╝    ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                 built by @Necrownyx</pre>


# PingServer

PingServer is a python package that makes things more convenient to set up a server to be pinged by uptimerobot.com this package is most useful on sites like replit.com where your program might shut down after being idle for too long


# Usage

First import the package with:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install PingServer`

Then import it with:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`import PingServer`

Then add this one line to start the server:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.start()`

The `start()` command has an optional parameter for a message on the web page to be pinged.

## How to run on a thread.
If you want to run the server on its own thread you can put this in your code:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.thread().start()`

This module of the package can also take a custom message for example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.thread("hello, world!").start()`

Will output "hello, world!" on the webpage.

## How to serve multiple pages.
If you want to serve multiple different pages first create the page use either:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.create_page(route, message)`

with `route` being the route of the site for example: `'/'`  and `message` being the message to be served to users or a html file name for example `index.html` this file must be in the templates directory of your project.

You can loop through this as many times as you want.

Then when you have defined all of the pages for your site run:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.launch_pages().start()`

To run all the sites on a thread or:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PingServer.launch_pages_nothread()`

To run the sites on the main thread.



## Background.

This is the first python package I have ever made and is somewhat of a tutorial for myself with something I will be able to use for things like discord bots on replit.com and more.
