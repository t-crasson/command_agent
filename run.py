from utils import deploy_agent, ask_request
from tools.final_answer import FinalAnswerTool
from tools.run_cmd import run_cmd
import argparse
import tools


def run():
    parser = argparse.ArgumentParser()

    parser.add_argument("request", type=str,  help="Request to the agent")
    parser.add_argument('--model_name', type=str, help="The model name",default="qwen2.5-coder:3b-instruct-q8_0")
    
    
    args = parser.parse_args()
    model_name = args.model_name
    request = args.request
    agent = deploy_agent(model_name,tools.list_function)
    request_answer = ask_request(agent,request)
    return request_answer

if __name__=="__main__":
    run()

