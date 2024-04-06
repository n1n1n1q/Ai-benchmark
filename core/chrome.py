from bs4 import BeautifulSoup
from distutils.version import LooseVersion
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os


RESPONSE_TIMEOUT = 10


def get_latest_chromedriver_path():
    try:
        home_dir = os.path.expanduser("~")
        sub_path = os.path.join("drivers", "chromedriver", "linux64")
        driver_name = "chromedriver"
        path = os.path.join(home_dir, ".wdm", sub_path)
        subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
        # Extract versions from the folder names
        versions = [folder.split(os.sep)[-1] for folder in subfolders]
        # Compare versions and find the latest
        latest_version = str(max(LooseVersion(ver) for ver in versions))
        # Full path to the chromedriver with the latest version
        latest_chromedriver_path = os.path.join(path, latest_version, driver_name)
    except FileNotFoundError:
        latest_chromedriver_path = None
    return latest_chromedriver_path or ChromeDriverManager().install()


class ChromeClient(webdriver.Chrome):

    def __init__(self):
        service = Service(
            executable_path=get_latest_chromedriver_path(),
            log_path="tmp/geckodriver.log",
        )

        options = self.__create_options()
        super().__init__(options=options)
        self.actions = ActionChains(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def bs4(self, source=None, tab=None, features="html.parser"):
        """Return page or tabs's BeautifulSoup"""
        return BeautifulSoup(source or self.page_source, features)

    def get(self, url, timeout=RESPONSE_TIMEOUT):
        """Load page by url and wait untill body is loaded"""

        super().get(url)
        try:
            WebDriverWait(self, timeout=timeout, poll_frequency=1.5).until(
                EC.presence_of_element_located((By.XPATH, "/html/body"))
            )
        except UnexpectedAlertPresentException:
            pass

    @staticmethod
    def __create_options() -> ChromiumOptions:
        options = ChromiumOptions()
        options.add_experimental_option("detach", True)
        return options
