from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from core.context import SeleniumContext
from core.crawler import Crawler, Layer
from core.settings import CrawlingSettings


def process_base(context: SeleniumContext):
    for i in range(1, 9):
        context.current_node.add_children(
            f"kyu {i}",
            page_url=f"https://www.codewars.com/kata/search/?q=&r%5B%5D=-{i}",
        )


def process_kyu(context: SeleniumContext):
    client = context.fetch_current_node()
    sleep(0.5)
    client.actions.send_keys(Keys.PAGE_DOWN).perform()


crawler = Crawler(
    CrawlingSettings(
        base_url="https://www.codewars.com",
        queries_per_second=1,
        context_class=SeleniumContext,
        max_retries=1,
        debug=True,
        layers=[
            Layer(name="Base", process_function=process_base),
            Layer(name="Kyus", process_function=process_kyu),
        ],
    )
)
