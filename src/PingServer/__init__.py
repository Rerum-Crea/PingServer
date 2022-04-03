def start_server(**message):
  from flask import Flask
  from flask import Flask, render_template, redirect
  if message == {}:
    message = ":)"
  app = Flask('app')
  @app.route('/')
  def Start():
    return message
  app.run(host='0.0.0.0', port=6969)

def thread():
    from threading import Thread
    thread_data = Thread(target=start_server)
    return thread_data