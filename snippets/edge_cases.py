# E01 — Wrong decorators
class DecorParent:
    def __init__(self): ...
class DecorChild(DecorParent):
    @staticmethod
    def __init__():
        ...

# E02 — super in try/except (already present)
class TryParent:
    def __init__(self): ...
class TryChild(TryParent):
    def __init__(self):
        try:
            super().__init__()
        except Exception:
            pass

# E03 — Metaclass/__new__ magic
class NewParent:
    def __new__(cls):
        return super().__new__(cls)
class NewChild(NewParent):
    def __init__(self):
        ...
