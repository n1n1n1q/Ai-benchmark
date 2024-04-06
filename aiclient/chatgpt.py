from core.aiclient import AIClient, Response
from core.chrome import ChromeClient


class ChatGPTResponse(Response):

    def __init__(self, code: str):
        self.code = code


class ChatGPTClient(AIClient, ChromeClient):

    def send_message(self, message: str) -> Response:
        pass

    def chat_list(self) -> list[str]:
        pass

    def open_new_chat(self) -> str:
        pass

    def close_chat(self, name: str) -> None:
        pass
