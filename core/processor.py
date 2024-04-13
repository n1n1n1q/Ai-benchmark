from abc import ABC, abstractmethod
from typing import Type

from core.aiclient import AIClient
from core.problemclient import ProblemClient
from core.models import Problem


class Processor(ABC):

    def __init__(
        self, aiclient_class: Type[AIClient], problem_client_class: Type[ProblemClient]
    ):
        self.aiclient_class = aiclient_class
        self.problem_client_class = problem_client_class
        self.problems = Problem.select()

    def process(self):
        for problem in self.problems:
            self.process_problem(problem)

    @abstractmethod
    def process_problem(self, problem):
        pass
