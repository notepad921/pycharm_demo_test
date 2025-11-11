# M01 — Diamond, cooperative
class A:
    def __init__(self, x): ...
class M:
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
class B(A, M):
    def __init__(self, x):
        ...

# M02 — Mixin without __init__
class M2: 
    pass
class A2:
    def __init__(self, x): ...
class B2(M2, A2):
    def __init__(self, x):
        ...

# M03 — Base without __init__
class A3: 
    pass
class B3(A3):
    def __init__(self):
        ...

# M04 — Explicit parent call already present
class A4:
    def __init__(self, x): ...
class B4(A4):
    def __init__(self, x):
        A4.__init__(self, x)
