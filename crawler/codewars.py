import requests
from time import sleep

from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.context import SeleniumContext
from core.crawler import Crawler, Layer
from core.settings import CrawlingSettings

SCROLL_NUM = 10
WAIT_TIME = 0.5


def process_base(context: SeleniumContext):
    for i in range(1, 9):
        context.current_node.add_children(
            f"kyu {i}",
            page_url=f"https://www.codewars.com/kata/search/?q=&r%5B%5D=-{i}",
        )


def process_tasks(context: SeleniumContext):
    client = context.fetch_current_node()
    for _ in range(SCROLL_NUM):
        client.actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(WAIT_TIME)
    response = requests.get(client.current_url)
    soup = client.bs4(response.content, "html.parser")
    kyus = soup.findAll(attrs={"class": "ml-2"})
    for kyu in kyus:
        kyu_ = str(kyu)
        kyu_ = kyu_.split(" ")[2].split('"')[1]
        print(kyu)
        # print(f"LINK: https://www.codewars.com{kyu}")
        context.current_node.add_children(
            name=f"task {kyus.index(kyu)}", page_url=f"https://www.codewars.com{kyu_}"
        )


def process_kyu(context: SeleniumContext):
    client = context.fetch_current_node()
    sleep(WAIT_TIME)
    name = client.find_element(By.CLASS_NAME, "ml-2").text
    description = client.find_element(By.ID, "description").text
    tags = client.find_elements(By.CLASS_NAME, "keyword-tag")
    tags = [i.text for i in tags]
    kyu = {"name": name, "description": description, "tags": tags}
    print(tags)


crawler = Crawler(
    CrawlingSettings(
        base_url="https://www.codewars.com",
        queries_per_second=1,
        context_class=SeleniumContext,
        max_retries=1,
        debug=True,
        layers=[
            Layer(name="Base", process_function=process_base),
            Layer(name="Tasks", process_function=process_tasks),
            Layer(name="Kyu", process_function=process_kyu),
        ],
    )
)
