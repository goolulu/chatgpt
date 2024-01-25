import os
import json
from typing import List

from openai import OpenAI
import time
import httpx

from openai.types.beta import Assistant, assistant_create_params

from fmpData import available_functions
from entity.function import info, param

OPENAI_API_KEY = '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'

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = httpx.Client(proxy='http://127.0.0.1:1080')
client = OpenAI(http_client=client)


# 如果已经定义好了助手可以直接使用 assistant_id传值


def create_assistant(model: str) -> Assistant:
    tools = create_tools()
    # Creating an assistant with specific instructions and tools

    assistant = client.beta.assistants.create(
        instructions="Act as a financial analyst by accessing detailed financial data through the Financial Modeling Prep API. Your capabilities include analyzing key metrics, comprehensive financial statements, vital financial ratios, and tracking financial growth trends. use chinese answer question",
        model=model,
        tools=tools
    )

    return assistant


def create_tools() -> List[assistant_create_params.Tool]:
    tools = []

    functions = info.get_all_function()
    params = param.get_all_function_param()

    return tools


def receive_msg(msg: str) -> str:
    resp = ''

    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=msg
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

        # Add run steps retrieval here
        run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run.id)
        print("Run Steps:", run_steps)

        if run.status == "requires_action":
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = []

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name in available_functions:
                    function_to_call = available_functions[function_name]
                    output = function_to_call(**function_args)
                    tool_outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": output,
                    })

            # Submit tool outputs and update the run
            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread_id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )

        elif run.status == "completed":
            # List the messages to get the response
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            for message in messages.data:
                role_label = "user" if message.role == "user" else "Assistant"
                message_content = message.content[0].text.value
                if message.role == 'assistant':
                    resp += f'{message_content}\n'
                    print(f"{role_label}: {message_content}\n")
                    return resp
                print(f"{role_label}: {message_content}\n")
                # Exit the loop after processing the completed run

        elif run.status == "failed":
            print("Run failed.")
            resp = "Run failed."
            break

        elif run.status in ["in_progress", "queued"]:
            print(f"Run is {run.status}. Waiting...")
            time.sleep(5)  # Wait for 5 seconds before checking again

        else:
            print(f"Unexpected status: {run.status}")
            break
    return resp


# assistant = create_assistant("gpt-3.5-turbo-1106")
assistant_id = 'asst_djONOd3wRsu36uw7XZMIqBPb'
thread = client.beta.threads.create()
thread_id = thread.id
