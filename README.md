
# Command Line Agent

This repository is contains an AI agent that can run an LLM agent in your command line shell. 




## Python run

This code requires Ollama to be running on your machine. Please install first (follow this repo https://github.com/ollama/ollama). Second, install the requirements on a python 3.12.9 (mainly smolagents).
Then run:

```bash
  python run.py "What time is it?" --model_name MODEL_NAME
```
with MODEL_NAME the model you want to run. Please check Ollama webpage to find the right LLM for you.

## Docker run
For those who want to run this agent in a docker container, you can create a docker image:

```bash
  docker built -t agent_cmd .
  docker run --net host agent_cmd "What time is it?"
```

