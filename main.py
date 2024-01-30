from flask import Flask, request

from chatgpt import receive_msg
from config import client
from entity import get_tools
from entity.gpt.assistant import get_assistant
from entity.gpt.user_assistant import get_user_assistant, update_user_assistant

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route('/send_msg', methods=['POST'])
def ask_msg():
    resp = ''
    data_dict = request.get_json()
    user_assistant = get_user_assistant()
    if data_dict['msg']:
        resp = receive_msg(data_dict['msg'], user_assistant[0].thread_id, user_assistant[0].assistant_id)
    return resp


@app.route('/create_assistant', methods=['GET'])
def create_assistant():
    tools = get_tools()
    # Creating an assistant with specific instructions and tools
    assistant_config = get_assistant()[0]
    assistant = client.beta.assistants.create(
        instructions=assistant_config.instructions,
        model=assistant_config.model,
        tools=tools
    )
    update_user_assistant(assistant.id)
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
