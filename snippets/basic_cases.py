
# B01 — Single inheritance, no args
class A:
    def __init__(self):
        pass
class B(A):
    def __init__(self):
        pass

# B02 — Positional + default
class A2:
    def __init__(self, x, y=10): ...
class B2(A2):
    def __init__(self, x, y=20):
        self.y = y

# B03 — Keyword-only
class A3:
    def __init__(self, *, limit: int): ...
class B3(A3):
    def __init__(self, *, limit: int):
        """Doc."""
        self.limit = limit

# B04 — Positional-only (PEP 570)
class A4:
    def __init__(self, x, /, y): ...
class B4(A4):
    def __init__(self, x, /, y):
        ...

# B05 — Varargs passthrough
class A5:
    def __init__(self, *args, **kwargs): ...
class B5(A5):
    def __init__(self, a, *args, **kwargs):
        ...

# B06 — Different names
class A6:
    def __init__(self, user_id, active=True): ...
class B6(A6):
    def __init__(self, uid, *, active=True, **kw):
        ...

# B07 — Built-in parent
class A7(list):
    def __init__(self, iterable=()):
        super().__init__(iterable)
class B7(A7):
    def __init__(self, iterable=()):
        ...

# B08 — Exception subclass
class A8(Exception):
    def __init__(self, msg: str): ...
class B8(A8):
    def __init__(self, msg: str):
        ...
