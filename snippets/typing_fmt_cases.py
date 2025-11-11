# T01 — Docstring first
class PathParent:
    def __init__(self, path: str): ...
class PathChild(PathParent):
    def __init__(self, path: str):
        """Loads things."""
        ...

# T02 — Long signature, wrapping
class LongSigParent:
    def __init__(self, very_long_argument_name: str, *, flag: bool = False): ...
class LongSigChild(LongSigParent):
    def __init__(
        self,
        very_long_argument_name: str,
        *,
        flag: bool = False,
    ):
        ...

# T03 — Mutable default
class ItemsParent:
    def __init__(self, items=None): ...
class ItemsChild(ItemsParent):
    def __init__(self, items=None):
        ...
