from core.problemclient import ProblemClient, Output


class CodewarsClient(ProblemClient):

    def open_problem(self, problem) -> None:
        pass

    def set_code_input_text(self, code: str) -> None:
        pass

    def run_tests(self) -> None:
        pass

    def make_attempt(self) -> None:
        pass

    def get_output(self) -> Output:
        pass
