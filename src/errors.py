from typing import Callable


class UnrecognisedFunctionError(Exception):
    message_template = "No function with name '{}'"

    def __init__(self, function: str | Callable) -> None:
        self.func = function

    def __str__(self) -> str:
        cls = self.__class__

        if callable(self.func):
            return cls.message_template.format(self.func.__name__)
        return cls.message_template.format(self.func)
