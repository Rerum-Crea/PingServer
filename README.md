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

## Background

This is the first python package I have ever made and is somewhat of a tutorial for myself with something I will be able to use for things like discord bots on replit.com and more.