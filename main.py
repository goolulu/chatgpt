import os

from flask import Flask, request

from chatgpt import receive_msg
from config import client
from datasource.dataSourceConfig import Session
from entity import get_tools
from entity.gpt.assistant import get_assistant, get_assistant_byid
from entity.gpt.user_assistant import get_user_assistant, update_user_assistant, create_user_assistant, UserAssistant

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route('/send_msg', methods=['POST'])
def ask_msg():
    resp = ''
    data_dict = request.get_json()
    user_assistant = get_user_assistant()
    if not user_assistant:
        return "查询不到用户，检查用户是否配置助手或api.env配置文件"
    if data_dict['msg']:
        resp = receive_msg(data_dict['msg'], user_assistant.thread_id, user_assistant.assistant_id)
    return resp


@app.route('/create_assistant/<id>', methods=['GET'])
def create_assistant(id):
    user_id = os.environ.get('user_id')
    ua = get_user_assistant()
    if ua:
        return f'用户{user_id} 已经存在助手请删除'
    tools = get_tools()
    # Creating an assistant with specific instructions and tools
    assistant_config = get_assistant_byid(id)
    if not assistant_config:
        return f'没有改助手配置{id}'
    assistant = client.beta.assistants.create(
        instructions=assistant_config.instructions,
        model=assistant_config.model,
        tools=tools
    )
    thread = client.beta.threads.create()
    ua = UserAssistant(user_id=os.environ.get('user_id'), assistant_id=assistant.id, thread_id=thread.id)
    create_user_assistant(ua)
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
