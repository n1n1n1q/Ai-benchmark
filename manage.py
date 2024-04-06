from selenium.webdriver.support.wait import WebDriverWait

from core.chrome import ChromeClient


with ChromeClient() as client:

    client.get("https://chat.openai.com")
    input()