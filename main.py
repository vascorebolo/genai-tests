import os
#import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

print(os.environ['OPEN_AI_KEY'])