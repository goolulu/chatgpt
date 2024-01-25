from flask import Flask, request

from chatgpt import receive_msg

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route('/send_msg/', methods=['POST'])
def ask_msg():
    data_dict = request.get_json()
    resp = ''
    if data_dict['msg']:
        resp = receive_msg(data_dict['msg'])

    if not resp:
        resp = "调用错误"

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
