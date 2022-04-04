class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def start(message=":)", route='/'):
    from flask import Flask, render_template, redirect
    import random

    app = Flask('app')

    @app.route('/')
    def server():
        return message

    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def thread(message=":)"):
    from threading import Thread
    thread_data = Thread(target=start, args=(message,))
    return thread_data

def launch_pages():
    from threading import Thread
    thread_data = Thread(target=launch_pages_internals())
    return thread_data

def launch_pages_internals():
    from flask import Flask, render_template, redirect
    import random

    app = Flask('app')

    @app.route(route_message[0]["route"])
    def Server_0():
        return route_message[0]["message"]

    @app.route(route_message[1]["route"])
    def Server_1():
        return route_message[1]["message"]

    @app.route(route_message[2]["route"])
    def Server_2():
        return route_message[2]["message"]

    @app.route(route_message[3]["route"])
    def Server_3():
        return route_message[3]["message"]

    @app.route(route_message[4]["route"])
    def Server_4():
        return route_message[4]["message"]

    @app.route(route_message[5]["route"])
    def Server_5():
        return route_message[5]["message"]

    @app.route(route_message[6]["route"])
    def Server_6():
        return route_message[6]["message"]

    @app.route(route_message[7]["route"])
    def Server_7():
        return route_message[7]["message"]

    @app.route(route_message[8]["route"])
    def Server_8():
        return route_message[8]["message"]

    @app.route(route_message[9]["route"])
    def Server_9():
        return route_message[9]["message"]

    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def initialize(amt=10, done=False):
    if not done:
        global route_message
        global pagenum
        pagenum = 10
        route_message = {}
        for i in range(10):
            route_message[i] = {}
            route_message[i]["route"] = '/Pingserver_initialize_page_default'
            route_message[i]["message"] = "No text channels You find yourself in a strange place. You don't have " \
                                          "access to any text channels, or there are none on this server. There is " \
                                          "nothing there, Everyone still have the server but cant just see it. "
        done = True
        return True
    else:
        try:
            pagenum -= 1
            return True
        except NameError:
            print(f"{bcolors.FAIL}##############################################")
            print(f"{bcolors.FAIL}You need to run PingServer.initialize() first.")
            print(f"{bcolors.FAIL}##############################################")
            return False


def create_page(route='/', message=":)"):
    initialize(0, True)
    if pagenum >= 0:
        route_message[pagenum]["route"] = route
        route_message[pagenum]["message"] = message
    else:
        print(f"{bcolors.WARNING}No Pages Left to use :(")
