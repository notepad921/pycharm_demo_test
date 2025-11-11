# B01 — Single inheritance, no args
class ParentNoArgs:
    def __init__(self):
        pass
class ChildNoArgs(ParentNoArgs):
    def __init__(self):
        pass

# B02 — Positional + default
class ParentPosDefault:
    def __init__(self, x, y=10): ...
class ChildPosDefault(ParentPosDefault):
    def __init__(self, x, y=20):
        self.y = y

# B03 — Keyword-only
class ParentKwOnly:
    def __init__(self, *, limit: int): ...
class ChildKwOnly(ParentKwOnly):
    def __init__(self, *, limit: int):
        """Doc."""
        self.limit = limit

# B04 — Positional-only (PEP 570)
class ParentPosOnly:
    def __init__(self, x, /, y): ...
class ChildPosOnly(ParentPosOnly):
    def __init__(self, x, /, y):
        ...

# B05 — Varargs passthrough
class ParentVarargs:
    def __init__(self, *args, **kwargs): ...
class ChildVarargs(ParentVarargs):
    def __init__(self, a, *args, **kwargs):
        ...

# B06 — Different names
class ParentDifferentNames:
    def __init__(self, user_id, active=True): ...
class ChildDifferentNames(ParentDifferentNames):
    def __init__(self, uid, *, active=True, **remaining_kwargs):
        ...

# B07 — Built-in parent
class ParentBuiltinList(list):
    def __init__(self, iterable=()):
        super().__init__(iterable)
class ChildBuiltinList(ParentBuiltinList):
    def __init__(self, iterable=()):
        ...

# B08 — Exception subclass
class ParentException(Exception):
    def __init__(self, msg: str): ...
class ChildException(ParentException):
    def __init__(self, msg: str):
        ...
