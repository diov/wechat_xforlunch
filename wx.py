# --coding:utf8--
import hashlib

from flask import Flask
from flask import make_response
from flask import request

from robot import robot

WX_TOKEN = 'x_forlunch'
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, Flask!'


@app.route('/wx', methods=['GET', 'POST'])
def wx_auth():
    if request.method == 'GET':
        token = WX_TOKEN
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        wx_list = [token, timestamp, nonce]
        wx_list.sort()
        wx_list = ''.join(wx_list)

        # sha1加密算法
        if hashlib.sha1(wx_list.encode('utf8')).hexdigest() == signature:
            return make_response(echostr)
        else:
            return 'Auth failed!'

    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.add_url_rule(rule='/wx', view_func=make_response(robot), methods=['GET', 'POST'])
    app.run(port=5601)
