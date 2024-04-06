from selenium.webdriver.common.by import By

from core.context import SeleniumContext
from core.crawler import Crawler, Layer
from core.settings import CrawlingSettings


def process_base(context: SeleniumContext):
    client = context.fetch_current_node()
    client.find_element(By.CSS_SELECTOR, ".text-color-hero-gradient")


crawler = Crawler(
    CrawlingSettings(
        base_url="https://www.codewars.com/",
        queries_per_second=1,
        context_class=SeleniumContext,
        max_retries=1,
        debug=True,
        layers=[
            Layer(name="Base", process_function=process_base),
        ])
)
