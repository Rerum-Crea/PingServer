def start(message=":)"):
  from flask import Flask
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