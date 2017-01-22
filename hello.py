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
        # sha1加密算法
        wx_sha1 = hashlib.sha1()
        map(wx_sha1.update, wx_list)
        w_hashcode = wx_sha1.hexdigest()

        if w_hashcode == signature:
            return make_response(echostr)

    if request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(port=5601)
