"""
Management script for AI analyzer
"""

import sys
import argparse
import importlib


class ArgumentsException(Exception):
    pass


def crawl():
    """Crawl"""
    if args.crawler_name is None:
        raise ArgumentsException("Crawler name is required")

    sys.path.append("core")
    sys.path.append("crawlers")

    try:
        crawler_module = importlib.import_module(f"crawler.{args.crawler_name}")
        crawler = getattr(crawler_module, "crawler")
    except (AttributeError, ModuleNotFoundError):
        raise ArgumentsException(f"There is no such crawler: {args.crawler_name}")

    crawler.crawl()


ACTIONS = {
    "crawl": crawl,
}

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("action", choices=ACTIONS)
argument_parser.add_argument("--crawler-name", help="Crawler name", required=False)

args = argument_parser.parse_args()

try:
    ACTIONS[args.action]()
except ArgumentsException as ex:
    print(str(ex))
except KeyError:
    print("There is no such command")
