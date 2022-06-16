from typing import Callable, TypeAlias

from functions import functions, N
from patterns import patterns
from errors import UnrecognisedFunctionError

number: TypeAlias = int | float | complex
null_var = object()


class Interpreter:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.script = list(map(str.strip, open(filename).readlines()))

        self.variables = {}

    def interpret(self, source: str = None, is_line: bool = False):
        if source is None:
            source = self.script

        if is_line:
            source = [source]

        for line in source:
            if line.strip() == "":
                continue

            self.check_print(line)

            var = self.find_variable(line)
            func = self.find_function(line)
            args = self.find_function_args(line)

            self.variables[var] = func(list(map(float, args)))

        line = self.replace_inline_variables(line)

        # Nothing to interpret
        return " ".join(source)

    def check_print(self, line: str):
        if line.startswith(">>"):
            print(self.interpret(line.replace(">> ", "", 1), is_line=True))

    def find_variable(self, line: str) -> str:
        try:
            return patterns["variable"].search(line).group(0)
        except AttributeError:
            return null_var

    def find_function(self, line: str) -> Callable[[N], N]:
        match = patterns["function"].search(line)

        if not match:
            return lambda _: _

        func = functions.get(match.group(0))

        if func is None:
            raise UnrecognisedFunctionError(match.group(0))

        return func

    def find_function_args(self, line: str) -> list[number]:
        match = patterns["function_args"].search(line)

        if not match:
            return []

        args = match.group(0).replace(" ", "").split(",")

        return args

    def replace_inline_variables(self, line: str) -> str:
        inline_vars = patterns["inline_variables"].findall(line)

        for var in inline_vars:
            start = line.index(var)

            if line[start - 1] == "$":
                print("iv")
                line.replace(line[start - 1: start + len(var)],
                             str(self.variables.get(var)))

        return line


def main():
    interpreter = Interpreter("script.mgsl")
    interpreter.interpret()


if __name__ == "__main__":
    main()
