from .launch_pages_internal import bcolors, create_page, launch_pages, initialize


def start(message=":)", route='/'):
    from flask import Flask
    import random

    app = Flask('app')

    @app.route(route)
    def server():
        return message

    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def thread(message=":)", route='/', daemon=False):
    from threading import Thread
    thread_data = Thread(target=start, args=(message, route), daemon=daemon)
    return thread_data


class help:
    def __init__(self):
        print(f"{bcolors.OKCYAN}###########################################################")
        print(f"{bcolors.OKCYAN}To get info on the different modules please goto:")
        print(f"{bcolors.OKCYAN}https://github.com/Necrownyx/PingServer/blob/main/README.md")
        print(f"{bcolors.OKCYAN}###########################################################")
