# Imports only the PingServer package to create, start, and run the servers on a thread. You might need to goto the
# shell and import PingServer with: pip import pingserver==0.0.20 The version is because I actively work on the
# package and sometimes there are bugs with the code and this is the current most stable version at the time of
# writing this. Documentation at https://pypi.org/project/PingServer/

from time import time
import PingServer


def func():
    return str(time())


PingServer.start('/', str(time()))
PingServer.launch_pages().start()

