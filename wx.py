# --coding:utf8--
import hashlib

from flask import Flask
from flask import request
from werobot.contrib.flask import make_view

from robot import robot

WX_TOKEN = 'x_forlunch'

app = Flask(__name__)
app.debug = True
app.add_url_rule(rule='/wx', view_func=make_view(robot), methods=['GET', 'POST'])


@app.route('/')
def hello_world():
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(port=5601)
