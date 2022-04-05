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
    thread_data = Thread(target=launch_pages_internals)
    return thread_data


def launch_pages_internals():
    from flask import Flask, render_template
    import random

    app = Flask('app')
    if pagenum >= 1:
        @app.route(route_message_html[0]["route"])
        def Server_0():
            return render_template(route_message_html[0]["html-path"])

        @app.route(route_message_html[1]["route"])
        def Server_1():
            return render_template(route_message_html[1]["html-path"])

        @app.route(route_message_html[2]["route"])
        def Server_2():
            return render_template(route_message_html[2]["html-path"])

        @app.route(route_message_html[3]["route"])
        def Server_3():
            return render_template(route_message_html[3]["html-path"])

        @app.route(route_message_html[4]["route"])
        def Server_4():
            return render_template(route_message_html[4]["html-path"])
    if pagenum >= 5:
        @app.route(route_message_html[5]["route"])
        def Server_5():
            return render_template(route_message_html[5]["html-path"])

        @app.route(route_message_html[6]["route"])
        def Server_6():
            return render_template(route_message_html[6]["html-path"])

        @app.route(route_message_html[7]["route"])
        def Server_7():
            return render_template(route_message_html[7]["html-path"])

        @app.route(route_message_html[8]["route"])
        def Server_8():
            return render_template(route_message_html[8]["html-path"])

        @app.route(route_message_html[9]["route"])
        def Server_9():
            return render_template(route_message_html[9]["html-path"])
    if pagenum >= 1:
        @app.route(route_message[0]["route"])
        def Server_10():
            return route_message[0]["message"]

        @app.route(route_message[1]["route"])
        def Server_11():
            return route_message[1]["message"]

        @app.route(route_message[2]["route"])
        def Server_12():
            return route_message[2]["message"]

        @app.route(route_message[3]["route"])
        def Server_13():
            return route_message[3]["message"]

        @app.route(route_message[4]["route"])
        def Server_14():
            return route_message[4]["message"]
    if pagenum >= 5:
        @app.route(route_message[5]["route"])
        def Server_15():
            return route_message[5]["message"]

        @app.route(route_message[6]["route"])
        def Server_16():
            return route_message[6]["message"]

        @app.route(route_message[7]["route"])
        def Server_17():
            return route_message[7]["message"]

        @app.route(route_message[8]["route"])
        def Server_18():
            return route_message[8]["message"]

        @app.route(route_message[9]["route"])
        def Server_19():
            return route_message[9]["message"]

    app.run(host='0.0.0.0', port=random.randint(2000, 9000))

def initialize_internals(amt=10, done=False, html=False):
    if not done:
        global route_message_html
        global route_message
        global pagenum
        if html == False:
            pagenum = 10
            route_message = {}
            for i in range(10):
                route_message[i] = {}
                route_message[i]["route"] = '/Pingserver_initialize_page_default'
                route_message[i]["message"] = "No text channels You find yourself in a strange place. You don't have " \
                                              "access to any text channels, or there are none on this server. There " \
                                              "is nothing there, Everyone still have the server but cant just see it. "
            done = True
            return True
        else:
            pagenum = 10
            route_message_html = {}
            for i in range(10):
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
            pagenum -= 1
            return True
        except NameError:
            print(f"{bcolors.FAIL}##############################################")
            print(f"{bcolors.FAIL}You need to run PingServer.initialize() first.")
            print(f"{bcolors.FAIL}##############################################")
            return False


def initialize(amt=10):
    initialize_internals(amt, False, False)
    initialize_internals(amt, False, True)


def create_page(route='/', message=":)"):
    initialize_internals(0, True)
    if pagenum >= 0:
        route_message[pagenum]["route"] = route
        route_message[pagenum]["message"] = message
    else:
        print(f"{bcolors.WARNING}No Pages Left to use :(")


def create_page_html(route='/', htmlpath=":)"):
    initialize_internals(0, True)
    if pagenum >= 0:
        route_message_html[pagenum]["route"] = route
        route_message_html[pagenum]["html-path"] = htmlpath
    else:
        print(f"{bcolors.WARNING}No Pages Left to use :(")


class help:
    def __init__(self):
        print(f"{bcolors.OKCYAN}###########################################################")
        print(f"{bcolors.OKCYAN}To get info on the different modules please goto:")
        print(f"{bcolors.OKCYAN}https://github.com/Necrownyx/PingServer/blob/main/README.md")
        print(f"{bcolors.OKCYAN}###########################################################")