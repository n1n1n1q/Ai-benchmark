"""
Crawling settings class
"""


class CrawlingSettings:
    """
    Settings of crawling
    """

    def __init__(
        self,
        base_url: str,
        queries_per_second: int,
        context_class,
        debug: bool = False,
        layers: list | None = None,
        max_retries: int = 3,
    ):

        self.base_url = base_url
        self.queries_per_second = queries_per_second

        self.context_class = context_class
        self.inputs = {}
        self.debug = debug
        self.layers = layers or []
        self.max_retries = max_retries
