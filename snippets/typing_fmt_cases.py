# T01 — Docstring first
class A:
    def __init__(self, path: str): ...
class B(A):
    def __init__(self, path: str):
        """Loads things."""
        ...

# T02 — Long signature, wrapping
class A2:
    def __init__(self, very_long_argument_name: str, *, flag: bool = False): ...
class B2(A2):
    def __init__(
        self,
        very_long_argument_name: str,
        *,
        flag: bool = False,
    ):
        ...

# T03 — Mutable default
class A3:
    def __init__(self, items=None): ...
class B3(A3):
    def __init__(self, items=None):
        ...
