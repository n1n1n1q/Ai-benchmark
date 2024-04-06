from __future__ import annotations

import hashlib
import time

from bs4 import BeautifulSoup


class Node:
    """Page representation"""

    def __init__(self, name=None, parent: Node = None, page_url=None,
                 page_content=None, node_id=None, layer=0):
        self.name = name
        self.node_id = node_id if node_id else hashlib.md5(self.name.encode()).hexdigest()
        self.page_url = page_url
        self.page_content = page_content
        self.properties = {}
        self.layer = layer

        self.parent = parent
        self.children = []

        self.locked = False

        self.cached_ancestor_chain = []

        self.__clean_name()

    def __str__(self):
        return f"<Node: {self.name}>"

    def __repr__(self):
        return str(self)

    def pop(self):
        """Remove self node from tree"""
        if self.parent:
            self.parent.remove_child(self)

    def add_children(self, name, page_url=None, page_content=None, node_id=None) -> Node:
        """Add child pages"""
        if page_url:
            new_node = Node(name=name, page_url=page_url, node_id=node_id)
        else:
            new_node = Node(name=name, page_content=page_content)
        new_node.parent = self
        new_node.layer = self.layer + 1
        self.children.append(new_node)
        return new_node

    def remove_child(self, child):
        """Remove child page"""
        if child not in self.children:
            return
        self.children.remove(child)
        if not self.children and self.parent:
            self.parent.remove_child(self)

    def fetch_content(self, context):
        """Fetch content of page"""
        page = context.make_request(self.page_url)
        self.page_content = BeautifulSoup(page.text, features="html.parser")
        context.last_fetch = time.time()

    def cache_ancestor_chain(self):
        """Save names list of parents"""
        self.cached_ancestor_chain = self.get_ancestor_chain()

    def get_ancestor_chain(self):
        """Get list of ancestor pages"""
        if not self.parent:
            return []
        else:
            if self.cached_ancestor_chain:
                return self.cached_ancestor_chain
            else:
                return self.parent.get_ancestor_chain() + [self]

    def get_properties_chain(self) -> list[dict]:
        """Return properties of this in and all ancestors"""
        return [node.properties for node in self.get_ancestor_chain()]

    def get_ancestor_path(self):
        """Return string of ancestor pages names"""
        return "/".join(map(lambda x: x.name, self.get_ancestor_chain()))

    def lock(self):
        """Lock node"""
        self.locked = True

    def unlock(self):
        """Unlock node"""
        self.locked = False

    def is_locked(self):
        """Return True if node is locked"""
        return self.locked

    def __clean_name(self):
        self.name = self.name.replace("/", " ")


class Tree:
    """Tree of page nodes"""

    def __init__(self):
        self.root = None

    def add_root_node(self, name, page_url):
        """Add root node by name and page_url"""
        self.root = Node(name=name, page_url=page_url)
        return self.root

    def set_root_node(self, node):
        """Set root node"""
        self.root = node
