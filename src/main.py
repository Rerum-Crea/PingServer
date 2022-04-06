# Imports only the PingServer package to create, start, and run the servers on a thread. You might need to goto the
# shell and import PingServer with: pip import pingserver==0.0.20 The version is because I actively work on the
# package and sometimes there are bugs with the code and this is the current most stable version at the time of
# writing this. Documentation at https://pypi.org/project/PingServer/


import PingServer


# Initialize the servers for the branches of the app.
PingServer.initialize(10)


# Sets up a page that serves an HTML file on the '/' branch.
PingServer.create_page('/', "index.html")


# Sets up a page that serves a string on the '/default' branch.
PingServer.create_page('/default', ':)')


# Launches all the pages set up above on a separate thread of code.
PingServer.launch_pages().start()


# Prints something to prove that it is on a different branch
print("It's on a different branch!!!")


# Notice how this code runs extremely fast this is because the servers are only loaded when you run the launch_pages() function.