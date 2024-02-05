import json

import openai
from dotenv import load_dotenv
from interface.terminal import pretty_print_conversation

from function.dalle_executor import generate_image
from function.linkedin_executor import make_post_linkedin
from function.twitter_executor import make_post_twitter
from instructions.system_instructions import LLM_INSTRUCTIONS
from tools import tools

# from messages_demo import messages

load_dotenv()
client = openai


def add_numbers(num1, num2):
    return num1 + num2


def execute_function(function_name, tool_call):
    available_functions = {
        "add_numbers": add_numbers,
        "generate_image": generate_image,
        "make_post_linkedin": make_post_linkedin,
        "make_post_twitter": make_post_twitter,
    }
    if not function_name:
        return f"function {function_name} not available for calling"
    if function_name == "add_numbers":
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(
            num1=function_args.get("num1"),
            num2=function_args.get("num2"),
        )
    if function_name == "generate_image":
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        function_response = function_to_call(
            prompt=function_args.get("prompt"),
        )
        pretty_print_conversation(
            messages=None, message=function_args.get("prompt")
        )
        # print(f"Function Response: {function_response}")
    if function_name == "make_post_linkedin":
        function_response = _extracted_from_execute_function_27(
            available_functions, function_name, tool_call, "linkedin_post"
        )
    if function_name == "make_post_twitter":
        function_response = _extracted_from_execute_function_27(
            available_functions, function_name, tool_call, "twitter_post"
        )
    return function_response


# TODO Rename this here and in `execute_function`
def _extracted_from_execute_function_27(available_functions, function_name, tool_call, arg3):
    function_to_call = available_functions[function_name]
    function_args = json.loads(tool_call.function.arguments)
    result = function_to_call(text=function_args.get(arg3))
    pretty_print_conversation(messages=None, message=function_args.get(arg3))
    return result


def init_chat():
    return [
        {"role": "system", "content": LLM_INSTRUCTIONS},
    ]


def chatbot(messages):

    # message = prompt
    # Add each new message to the list
    # messages.append({"role": "user", "content": message})
    pretty_print_conversation(messages=messages, message=None)

    # Request gpt-3.5-turbo for chat completion
    response = client.chat.completions.create(
        model="gpt-4-1106-preview", 
        messages=messages, 
        tools=tools, 
        tool_choice="auto"
    )

    # Print the response and add it to the messages list
    # print(response)
    response_message = response.choices[0].message
    if tool_calls := response_message.tool_calls:
        _extracted_from_chatbot_(messages, response_message, tool_calls)
    else:
        chat_message = response_message.content
        # print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})
        # print(messages)
        pretty_print_conversation(messages=messages, message=None)
    return messages


# TODO Rename this here and in `chatbot`
def _extracted_from_chatbot_(messages, response_message, tool_calls):
    tool_messages = messages.copy()
    # Initialise another array for tool content
    tool_messages.append(response_message)
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        pretty_print_conversation(messages=None, message=f"Calling {function_name}")
        function_response = execute_function(function_name, tool_call)
        tool_messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": str(function_response),
            }
        )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-4-0613",
            messages=tool_messages,
        )
        final_response = second_response.choices[0].message.content
    chat_message = final_response

    messages.append({"role": "assistant", "content": chat_message})
    pretty_print_conversation(messages=messages, message=None)