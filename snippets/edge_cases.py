# E01 — Wrong decorators
class A:
    def __init__(self): ...
class B(A):
    @staticmethod
    def __init__():
        ...

# E02 — super in try/except (already present)
class A2:
    def __init__(self): ...
class B2(A2):
    def __init__(self):
        try:
            super().__init__()
        except Exception:
            pass

# E03 — Metaclass/__new__ magic
class A3:
    def __new__(cls):
        return super().__new__(cls)
class B3(A3):
    def __init__(self):
        ...
