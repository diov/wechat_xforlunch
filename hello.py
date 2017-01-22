# --coding:utf8--
import hashlib

from flask import Flask
from flask import make_response
from flask import request

WX_TOKEN = 'x_forlunch'
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, Flask!'


@app.route('/wx', methods=['GET', 'POST'])
def wx_auth():
    if request.method == 'GET':
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = WX_TOKEN
        wx_list = [token, timestamp, nonce]
        wx_list.sort()
        wx_list = ''.join(wx_list)
        # sha1加密算法

        if (hashlib.sha1(wx_list.encode('utf8')).hexdigest() == signature):
            return make_response(echostr)
        else:
            return '{0}: {1}'.format(signature, w_hashcode)

    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(port=5601)
