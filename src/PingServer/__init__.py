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
    from .launch_pages_internal import launch_pages_internals
    thread_data = Thread(target=launch_pages_internals, args=(route_message_html, route_message, pageamt, htmlpageamt))
    return thread_data


def initialize_internals(amt=10, done=False, html=False):
    if not done:
        global route_message_html
        global route_message
        global pagenum
        global htmlpagenum
        global pageamt
        global htmlpageamt
        if not html:
            pagenum = amt
            pageamt = amt
            route_message = {}
            for i in range(amt):
                route_message[i] = {}
                route_message[i]["route"] = '/Pingserver_initialize_page_default'
                route_message[i]["message"] = "No text channels You find yourself in a strange place. You don't have " \
                                              "access to any text channels, or there are none on this server. There " \
                                              "is nothing there, Everyone still have the server but cant just see it. "
            done = True
            return True
        else:
            htmlpagenum = amt
            htmlpageamt = amt
            route_message_html = {}
            for i in range(amt):
                route_message_html[i] = {}
                route_message_html[i]["route"] = '/Pingserver_initialize_page_default'
                route_message_html[i]["html-path"] = "No text channels You find yourself in a strange place. You don't " \
                                                     "have access to any text channels, or there are none on this " \
                                                     "server. There is nothing there, Everyone still have the server " \
                                                     "but cant just see it. "
            done = True
            return True
    else:
        try:
            if not html:
                pagenum -= 1
                return True
            else:
                htmlpagenum -= 1
                return False
        except NameError:
            print(f"{bcolors.FAIL}##############################################")
            print(f"{bcolors.FAIL}You need to run PingServer.initialize() first.")
            print(f"{bcolors.FAIL}##############################################")
            return "Run PingServer.initialize()"


def initialize(amt=10):
    initialize_internals(amt, False, False)
    initialize_internals(amt, False, True)


def create_page(route='/', message=":)"):
    initialize_internals(0, True, False)
    if pagenum >= 0:
        route_message[pagenum]["route"] = route
        route_message[pagenum]["message"] = message
    else:
        print(f"{bcolors.WARNING}No Pages Left to use :(")


def create_page_html(route='/', htmlpath=":)"):
    initialize_internals(0, True, True)
    if htmlpagenum >= 0:
        route_message_html[pagenum]["route"] = route
        route_message_html[pagenum]["html-path"] = htmlpath
    else:
        print(f"{bcolors.WARNING}No HTML Pages Left to use :(")


class help:
    def __init__(self):
        print(f"{bcolors.OKCYAN}###########################################################")
        print(f"{bcolors.OKCYAN}To get info on the different modules please goto:")
        print(f"{bcolors.OKCYAN}https://github.com/Necrownyx/PingServer/blob/main/README.md")
        print(f"{bcolors.OKCYAN}###########################################################")
