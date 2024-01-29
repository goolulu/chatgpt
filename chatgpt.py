import json
import logging
import os
import time

import httpx
from openai import OpenAI
from openai.types.beta import Assistant

from entity import get_tools
from fmpData import available_functions

OPENAI_API_KEY = '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'

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = httpx.Client(proxy='http://127.0.0.1:1080')
client = OpenAI(http_client=client)


def create_assistant(model: str) -> Assistant:
    tools = get_tools()
    # Creating an assistant with specific instructions and tools

    assistant = client.beta.assistants.create(
        instructions="Act as a financial analyst by accessing detailed financial data through the Financial Modeling Prep API. Your capabilities include analyzing key metrics, comprehensive financial statements, vital financial ratios, and tracking financial growth trends. use chinese answer question",
        model=model,
        tools=tools
    )
    return assistant


def receive_msg(msg: str, thread_id, assistant_id) -> str:
    resp = ''

    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=msg
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    try:
        resp = run_assistan(run)
    except Exception as e:
        logging.error(e)
        client.beta.threads.runs.cancel(run_id=run.id, thread_id=thread_id)
    return resp


def run_assistan(run):
    resp = ''
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
                function_args['apikey'] = os.environ.get("apikey")
                if function_name in available_functions:
                    function_to_call = available_functions[function_name]
                    output = function_to_call(**function_args)
                    if not isinstance(output, str):
                        output = json.dumps(output)

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


# assistant = create_assistant("gpt-3.5-turbo-1106")
assistant_id = 'asst_IIV6hcqRXjxQlTQGsaJn1V5n'
thread = client.beta.threads.create()
thread_id = thread.id
