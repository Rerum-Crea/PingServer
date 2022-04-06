from .launch_pages_internal import bcolors, create_page, launch_pages, launch_pages_nothread


def start(route="/", message=':)', port=6969, amount=1):
    import random
    if port == 6969:
        port = random.randint(2000, 9000)
    create_page(route, message)
    launch_pages_nothread(port)


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