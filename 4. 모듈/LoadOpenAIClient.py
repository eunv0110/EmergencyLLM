# 0. load key file------------------\
import os
import openai
def LoadOpenAIClient(filepath):
    with open(filepath + 'api_key.txt', 'r') as file:
        openai.api_key = file.readline().strip()
    os.environ['OPENAI_API_KEY'] = openai.api_key
    c = OpenAI()
    return c