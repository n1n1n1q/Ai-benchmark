from aiclient.chatgpt import ChatGPTClient
from core.processor import Processor
from problemclient.codewarsclient import CodewarsClient


class CodewarsProcessor(Processor):

    def process_problem(self, problem):
        print(123)

processor = CodewarsProcessor(aiclient_class=ChatGPTClient, problem_client_class=CodewarsClient)

