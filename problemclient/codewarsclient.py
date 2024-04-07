from selenium.webdriver.common.by import By

from core.chrome import ChromeClient
from core.problemclient import ProblemClient, Output


class CodewarsOutput(Output):
    pass


class CodewarsClient(ChromeClient, ProblemClient):

    def open_problem(self, problem_url: str) -> None:
        pass

    def set_code_input_text(self, code: str) -> None:
        pass

    def run_tests(self) -> None:
        pass

    def make_attempt(self) -> None:
        pass

    def get_output(self) -> Output:
        pass
