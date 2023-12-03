import io
import sys
from flask import Flask, jsonify
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from contextlib import contextmanager

app = Flask(__name__)

# @contextmanager
# def capture_output():
#     new_out = io.StringIO()
#     old_out = sys.stdout
#     try:
#         sys.stdout = new_out
#         yield new_out
#     finally:
#         sys.stdout = old_out

# Your existing setup for AutoGen
config_list = [
    {
        'model': 'gpt-4',
        'api_key': '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'  # Replace with your actual API key
    },
]
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

@app.route('/get-response', methods=['GET'])
def get_response():
    # Initiates an automated chat between the two agents to solve the task
     #return jsonify({"output": user_proxy.initiate_chat(
     #   assistant,
     #   message="Plot a chart of NVDA and TESLA stock price change YTD."
    #)})
    user_proxy.initiate_chat(
         assistant,
         message="Plot a chart of NVDA and TESLA stock price change YTD."
    )

    return user_proxy.last_message()

if __name__ == '__main__':
    app.run(debug=True)

