from flask import Flask
from flask import Flask, render_template

def start_server(**message):
  if message == {}:
    message = ":)"
  app = Flask('app')
  @app.route('/')
  def Start():
    return message

  app.run(host='0.0.0.0', port=6969)
