from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.aiclient import AIClient, Response
from core.chrome import ChromeClient


class ChatGPTResponse(Response):

    def __init__(self, code: str):
        self.code = code


class ChatGPTClient(ChromeClient, AIClient):

    def __init__(self):
        super().__init__()
        self.get("https://chat.openai.com/")

    def send_message(self, message: str) -> Response:
        pass

    def chat_list(self) -> list[str]:
        pass

    def open_new_chat(self) -> str:
        pass

    def close_chat(self, name: str) -> None:
        pass
