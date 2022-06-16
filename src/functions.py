from statistics import geometric_mean as _geometric_mean
from statistics import harmonic_mean as _harmonic_mean
from statistics import mean as _arithmetic_mean
from typing import Callable, TypeVar

N = TypeVar("N", int, float, complex)


functions: dict[str, Callable[[N], N]] = {
    "amean": lambda i: _arithmetic_mean(i),
    "gmean": lambda i: _geometric_mean(i),
    "hmean": lambda i: _harmonic_mean(i),
}
