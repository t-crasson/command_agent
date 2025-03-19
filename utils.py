from smolagents import ToolCallingAgent,LiteLLMModel, ActionStep, TaskStep, PlanningStep

import os
import tools
from typing import Any, Callable, Dict, Generator, List, Optional, Set, Tuple, TypedDict, Union





def get_agent(model:LiteLLMModel,
              list_function:List):
    agent = ToolCallingAgent(
        tools=list_function,
        model=model
    )
    return agent


def stop_model(model_name:str):
    os.system("ollama stop " + model_name)


def get_model(model_name:str):
    model = LiteLLMModel(model_id="ollama/"+model_name,api_key=None,api_base="http://localhost:11434")
    return model


def question_agent(question:str,
                   agent:ToolCallingAgent):
    response = agent.run(question)
    return response


def ask_request(agent:ToolCallingAgent,
            request:str):
    response = agent.run(request)
    return response


def deploy_agent(model_name:str,
                 list_function:List
                 ):
    model = get_model(model_name=model_name)
    agent = get_agent(model = model,
                      list_function=list_function)
    return agent


    

