from abc import ABC, abstractmethod
from typing import List


class Response:
    pass


class ChatDoesNotExist(Exception):
    """Exception raised when we want to access chat that doesn't exist'"""


class AIClient(ABC):
    """Abstract class for AI Clients"""

    @abstractmethod
    def send_message(self, message: str) -> Response:
        """Send message to AI"""

    @abstractmethod
    def chat_list(self) -> list[str]:
        """
        :return: List of all chat names
        """

    @abstractmethod
    def open_new_chat(self) -> str:
        """
        Open new chat
        :return: name of new chat
        """

    @abstractmethod
    def close_chat(self, name: str) -> None:
        """
        Close existing chat
        :param name: name of chat
        :return: None
        :raises: ValueError if there is no such chat
        """
