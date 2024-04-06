from abc import ABC, abstractmethod


class Output:

    def __init__(self, text: str, passed_count: int, failed_count, total_time: int):

        self.text = text
        self.passed_count = passed_count
        self.failed_count = failed_count
        self.total_time = total_time


class ProblemClient(ABC):

    @abstractmethod
    def open_problem(self, problem) -> None:
        pass

    @abstractmethod
    def set_code_input_text(self, code: str) -> None:
        pass

    @abstractmethod
    def run_tests(self) -> None:
        pass

    @abstractmethod
    def make_attempt(self) -> None:
        pass

    @abstractmethod
    def get_output(self) -> Output:
        pass
