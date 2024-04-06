from abc import ABC, abstractmethod

from core.aiclient import AIClient
from core.problemclient import ProblemClient


class Processor(ABC):

    def __init__(self, aiclient: AIClient, problem_client: ProblemClient):
        self.aiclient = aiclient
        self.problem_client = problem_client
        self.problems = []

    def process(self):
        for problem in self.problems:
            self.process_problem(problem)

    @abstractmethod
    def process_problem(self, problem):
        pass
