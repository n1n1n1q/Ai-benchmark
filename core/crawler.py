"""Crawler module"""

from __future__ import annotations
import traceback
from settings import CrawlingSettings


class Layer:
    """Tree layer"""

    def __init__(self, name, process_function, multi_worker_processing=False):
        self.name = name
        self.process_function = process_function
        self.partition = multi_worker_processing


class CrawlerWorker:
    """
    Worker is entity that controlls crawling flow.
    i.e. decides explores node tree, acticates node processors
    """

    def __init__(self, context, root_node):
        self.context = context
        self.root_node = root_node

    def crawl(self):
        """Crawl starting form root node"""
        self.context.current_node = self.root_node
        self.context.tree.set_root_node(self.root_node)
        self.try_process_n_times(
            self.context.settings.layers[self.root_node.layer].process_function
        )

        deepest_node = self.find_unpocessed_node()
        while deepest_node != self.root_node:
            self.context.current_node = deepest_node

            print(
                "--" * deepest_node.layer,
                deepest_node.name,
                "==",
                deepest_node.parent.name,
                deepest_node.page_url,
            )

            self.try_process_n_times(
                self.context.settings.layers[deepest_node.layer].process_function
            )

            if not deepest_node.children:
                deepest_node.parent.remove_child(deepest_node)
            deepest_node = self.find_unpocessed_node()

    def try_process_n_times(self, process_function):
        """
        Try to start current_node processor several times
        If processor fails all time rethrow exception
        """
        counter = 0
        while True:
            try:
                process_function(self.context)
                break
            except Exception:  # pylint: disable=broad-except
                counter += 1
                if counter >= self.context.settings.max_retries:
                    trb = traceback.format_exc()
                    print(trb)
                    break

    def find_unpocessed_node(self):
        """Return deepest unprocessed node"""
        node = self.context.tree.root
        while node.children:
            node = node.children[0]
        return node


class Crawler:
    """Main Crawler class"""

    ROOT_LAYER_INDEX = 0

    def __init__(self, settings: CrawlingSettings):
        self.settings = settings

        self.context = self.settings.context_class(settings=settings)

        self.root_node = self.context.tree.add_root_node(
            name=self.settings.layers[Crawler.ROOT_LAYER_INDEX].name,
            page_url=self.context.settings.base_url,
        )
        self.context.current_node = self.root_node
        self.base_parser_worker = CrawlerWorker(self.context, root_node=self.root_node)

    def crawl(self):
        """Crawl starting from root node"""
        try:
            self.base_parser_worker.crawl()
        except Exception:  # pylint: disable=broad-except
            trb = traceback.format_exc()
            print(trb)
        except KeyboardInterrupt:
            print("Parsing is stopped!")
        finally:
            self.context.finish()
