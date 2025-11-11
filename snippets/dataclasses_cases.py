from dataclasses import dataclass

# D01 — Parent is @dataclass
@dataclass
class DataParent:
    id: int
    name: str = "n"

class DataChildExplicitInit(DataParent):
    def __init__(self, id: int, name: str = "n"):
        ...

# D02 — Child is @dataclass, no explicit __init__
class RegularParentWithInit:
    def __init__(self, x): ...
@dataclass
class DataChildAutoInit(RegularParentWithInit):
    x: int
