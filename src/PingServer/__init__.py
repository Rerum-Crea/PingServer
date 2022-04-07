from .launch_pages_internal import bcolors, create_page, launch_pages, launch_pages_nothread
import flask


def start(route="/", horm=':)', port=6969):
    import random
    if port == 6969:
        port = random.randint(2000, 9000)
    create_page(route, horm)
    launch_pages_nothread(port)


def thread(message=":)", route='/', port=6969, daemon=False):
    from threading import Thread
    thread_data = Thread(target=start, args=(route, message, port), daemon=daemon)
    return thread_data


class help:
    def __init__(self):
        print(f"{bcolors.OKCYAN}###########################################################")
        print(f"{bcolors.OKCYAN}To get info on the different modules please goto:")
        print(f"{bcolors.OKCYAN}https://github.com/Necrownyx/PingServer/blob/main/README.md")
        print(f"{bcolors.OKCYAN}###########################################################")