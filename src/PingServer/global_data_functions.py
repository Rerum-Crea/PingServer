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


def create_page(route='/', horm=':)'):
    global htmlpagenum
    global pagenum
    try:
        if not done:
            initialize(True)
        htmlpagenum = initialize(True)
        pagenum = initialize(False)
        if ".html" in horm:
            if htmlpagenum <= 50:
                route_message_html[htmlpagenum]["route"] = route
                route_message_html[htmlpagenum]["html-path"] = horm
                htmlpagenum += 1
            else:
                print(f"{bcolors.WARNING}No HTML Pages Left to use :(")
        else:
            if pagenum <= 50:
                route_message[pagenum]["route"] = route
                route_message[pagenum]["message"] = horm
                pagenum += 1
            else:
                print(f"{bcolors.WARNING}No Pages Left to use :(")
    except NameError:
        initialize(True)
        htmlpagenum = initialize(True)
        pagenum = initialize(False)
        if ".html" in horm:
            if htmlpagenum <= 50:
                route_message_html[htmlpagenum]["route"] = route
                route_message_html[htmlpagenum]["html-path"] = horm
                htmlpagenum += 1
            else:
                print(f"{bcolors.WARNING}No HTML Pages Left to use :(")
        else:
            if pagenum <= 50:
                route_message[pagenum]["route"] = route
                route_message[pagenum]["message"] = horm
                pagenum += 1
            else:
                print(f"{bcolors.WARNING}No Pages Left to use :(")


def launch_pages(port=6969, daemon=False):
    from threading import Thread
    from launch_pages import launch_pages_internals
    thread_data = Thread(target=launch_pages_internals, args=(port, route_message_html, route_message, pagenum, htmlpagenum), daemon=daemon)
    return thread_data


def launch_pages_nothread(port=6969):
    from .launch_pages import launch_pages_internals
    launch_pages_internals(port, route_message_html, route_message, pagenum, htmlpagenum)


def initialize(html):
    global route_message_html
    global route_message
    global pagenum
    global htmlpagenum
    global done
    try:
        done + 1
    except NameError:
        pagenum = 0
        htmlpagenum = 0
        route_message_html = {}
        route_message = {}
        for i in range(50):
            route_message_html[i] = {}
            route_message[i] = {}
            route_message_html[i]['route'] = '/PingServerIsTheBestForThingsLikeLongURLSJK'
            route_message[i]['route'] = '/PingServerIsTheBestForThingsLikeLongURLSJK'
            route_message_html[i]['message'] = ':('
            route_message[i]['html-path'] = 'If you use the default for html your bad'
        done = True
    if done is True:
        if html is True:
            return htmlpagenum
        else:
            return pagenum