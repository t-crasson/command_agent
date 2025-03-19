from typing import Any, Optional
from smolagents import tool
import subprocess
@tool
def run_cmd(command:list)-> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """This function runs command line on the system and retrieve the output of the command 
    Args:
        command: list of strings, where each string is either a command or a parameter
    """
    result = subprocess.run(command, capture_output=True, text=True)
    stdout = result.stdout
    stderr = result.stderr
    return_code = result.returncode
    if stdout != "":
        return f"The ouput of {command} is {stdout}"
    elif stderr != "":
        return f"The following error occured : {stderr}"
    else:
        return f"The following code was returned : {return_code}"