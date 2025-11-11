# D01 — Parent is @dataclass
from dataclasses import dataclass


@dataclass
class A:
    id: int
    name: str = "n"

class B(A):
    def __init__(self, id: int, name: str = "n"):
        ...

# D02 — Child is @dataclass, no explicit __init__
class A2:
    def __init__(self, x): ...
@dataclass
class B2(A2):
    x: int
