"""
Edge/negative scenarios intended to test absence of noise and misclassifications.
The quick-fix should NOT be suggested where it doesn't make semantic sense.
"""

# E01 — Wrong decorators
class DecorParent:
    """Valid parent; child misuses decorators on __init__."""
    def __init__(self):
        ...


class DecorChild(DecorParent):
    """
    @staticmethod on __init__ is semantically invalid; inspection should not
    propose 'Add superclass call'. E01.
    """
    @staticmethod
    def __init__():
        ...


# E02 — super in try/except (already present)
class TryParent:
    """Parent with trivial init. Used by E02."""
    def __init__(self):
        ...


class TryChild(TryParent):
    """
    Child already calls super() inside try/except. Inspection must be quiet; no fix.
    E02.
    """
    def __init__(self):
        try:
            super().__init__()
        except Exception:
            pass


# E03 — Metaclass/__new__ magic
class NewParent:
    """
    Parent implements __new__ only (no __init__). In this case the quick-fix should
    not be suggested because there is no parent __init__. E03.
    """
    def __new__(cls):
        return super().__new__(cls)


class NewChild(NewParent):
    """Child __init__ does not need to call a non-existent parent __init__. E03."""
    def __init__(self):
        ...


# -----------------------------
# E04 — Parent is object
# -----------------------------
class OnlyObject(object):
    """Parent is plain object; there is nothing meaningful to call. E04."""
    pass


class ChildOverObject(OnlyObject):
    """No inspection / no quick-fix expected (avoid noise). E04."""
    def __init__(self):
        ...


# -----------------------------
# E05 — Parent defines __init__ = object.__init__
# -----------------------------
class ParentAliasInit:
    """Parent effectively has no __init__ of its own. E05."""
    __init__ = object.__init__


class ChildAliasInit(ParentAliasInit):
    """No inspection / no quick-fix. E05."""
    def __init__(self):
        ...


# -----------------------------
# E06 — Conditional super() already present
# -----------------------------
class CondParent:
    """Parent accepts a flag used to conditionally initialize. E06."""
    def __init__(self, setup=True):
        ...


class CondChild(CondParent):
    """
    super() is already present under a condition; inspection should not
    propose another call. E06.
    """
    def __init__(self, setup=True):
        if setup:
            super().__init__(setup=setup)
