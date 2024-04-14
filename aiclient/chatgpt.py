"""
Framework to work with chat GPT
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.aiclient import AIClient, Response
from core.chrome import ChromeClient
from time import sleep


class ChatGPTResponse(Response):

    def __init__(self, code: str):
        self.code = code


class ChatGPTClient(ChromeClient, AIClient):

    def __init__(self):
        super().__init__()
        self.get("https://chat.openai.com/")

    def send_message(self, message: str) -> Response:
        print("Looking for input box")
        sleep(0.5)

        prompt_input = self.find_element(By.ID, "prompt-textarea")

        print("Started inputing")
        prompt_input.send_keys(message)
        sleep(0.5)
        print("Inputed text")

        sleep(0.5)
        print("Press enter")
        prompt_input.send_keys(Keys.ENTER)
        print("pressed Enter !!!")
        return

    def copy_code(self) -> Response:
        sleep(0.5)
        self.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div/pre/div/div[1]/span[2]/button",
        ).click()

        prompt_input = self.find_element(By.ID, "prompt-textarea")
        sleep(0.5)
        prompt_input.send_keys(Keys.CONTROL, "v")
        sleep(0.5)

    def chat_list(self) -> list[str]:
        pass

    def open_new_chat(self) -> str:
        pass

    def close_chat(self, name: str) -> None:
        pass
