"""
Module for contexts
"""
import time
import requests

from settings import CrawlingSettings
from crawler import Node, Tree


class Context:
    """
    Run context of crawling
    """

    def __init__(self, settings: CrawlingSettings):
        self.settings = settings
        self.current_node: Node = None
        self.last_fetch = 0
        self.tree = Tree()

    def is_request_permitted(self):
        """
        Return True if limit of queries per second isn't exceeded
        """
        delay = 1 / self.settings.queries_per_second
        if time.time() - self.last_fetch > delay:
            return True
        else:
            return False

    def fetch_current_node(self):
        """Fetch current's node page"""
        self.current_node.fetch_content(self)

    def make_request(self, url):
        """Make request to url"""
        response = None
        counter = 0
        if not self.is_request_permitted():
            while not self.is_request_permitted():
                pass

        while True:
            try:
                response = requests.get(url, timeout=10)
                break
            except Exception: # pylint: disable=broad-except
                counter += 1
                if counter > 10:
                    break
                time.sleep(2 * counter)
        return response
