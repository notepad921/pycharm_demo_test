"""
Basic scenarios for PyCharm inspection + quick-fix
'Add superclass call'. Each Parent*/Child* pair is isolated and
intentionally missing super().__init__ in the child to trigger the inspection.
"""

# -----------------------------
# B01 — Single inheritance, no args
# -----------------------------
class ParentNoArgs:
    """Parent defines a parameterless __init__() that prepares state. Used by B01."""

    def __init__(self):
        pass
        self.ready = True


class ChildNoArgs(ParentNoArgs):
    """Child lacks super().__init__(); quick-fix must insert it before touching parent state."""

    def __init__(self):
        pass
        self.is_ready = self.ready  # Quick-fix should insert super().__init__() before this line.


# -----------------------------
# B01a — Early parent dependency
# -----------------------------
class ParentRequiresSetup:
    """Parent initializes state that children may access immediately. B01."""

    def __init__(self):
        self.ready = True


class ChildEarlyDependency(ParentRequiresSetup):
    """Child touches parent-provided state; super() must precede that access."""

    def __init__(self):
        self.is_ready = self.ready  # Quick-fix should insert super().__init__() before this line.


# -----------------------------
# B02 — Positional + default
# -----------------------------
class ParentPosDefault:
    """Parent defines __init__(x, y=10). Used by B02."""
    def __init__(self, x, y=10):
        ...


class ChildPosDefault(ParentPosDefault):
    """Child re-declares (x, y=20); quick-fix should call super().__init__(x, y)."""
    def __init__(self, x, y=20):
        self.y = y


# -----------------------------
# B03 — Keyword-only
# -----------------------------
class ParentKwOnly:
    """Parent has keyword-only argument: __init__(*, limit: int). Used by B03."""
    def __init__(self, *, limit: int):
        ...


class ChildKwOnly(ParentKwOnly):
    """Child must call super().__init__(limit=limit) after docstring. B03."""
    def __init__(self, *, limit: int):
        """Docstring should remain the first statement in the body."""
        self.limit = limit


# -----------------------------
# B04 — Positional-only (PEP 570)
# -----------------------------
class ParentPosOnly:
    """Parent has positional-only x and normal y: __init__(x, /, y). Used by B04."""
    def __init__(self, x, /, y):
        ...


class ChildPosOnly(ParentPosOnly):
    """Child must pass x positionally: super().__init__(x, y). B04."""
    def __init__(self, x, /, y):
        ...


# -----------------------------
# B05 — Varargs passthrough
# -----------------------------
class ParentVarargs:
    """Parent accepts arbitrary args: __init__(*args, **kwargs). Used by B05."""
    def __init__(self, *args, **kwargs):
        ...


class ChildVarargs(ParentVarargs):
    """Child introduces 'a' but should forward the rest: super().__init__(*args, **kwargs)."""
    def __init__(self, a, *args, **kwargs):
        ...


# -----------------------------
# B06 — Different names
# -----------------------------
class ParentDifferentNames:
    """Parent expects (user_id, active=True). Used by B06."""
    def __init__(self, user_id, active=True):
        ...


class ChildDifferentNames(ParentDifferentNames):
    """
    Child uses different name 'uid' and provides **remaining_kwargs.
    Strategy: match by name where possible ('active'), don't pass the rest via **kwargs.
    Should NOT guess uid→user_id. B06.
    """
    def __init__(self, uid, active=True, **remaining_kwargs):
        ...


# -----------------------------
# B07 — Built-in parent (list)
# -----------------------------
class ParentBuiltinList(list):
    """Parent subclasses built-in `list` and delegates to list.__init__(iterable). Used by B07."""
    def __init__(self, iterable=()):
        super().__init__(iterable)


class ChildBuiltinList(ParentBuiltinList):
    """
    Child should call super().__init__(iterable).
    Expected: quick-fix inserts `super().__init__(iterable)` BEFORE we read len(self)."""

    def __init__(self, iterable=()):
     # EARLY RELIANCE: must be after super().__init__(iterable)
     self.initial_len_snapshot = len(self)
     ...


# -----------------------------
# B08 — Parent uses __slots__
# -----------------------------
class SlottedParent:
    """
    Parent defines __slots__ and initializes the slot in __init__.
    Missing super() in child should be detected. Quick-fix must insert
    super().__init__(token).
    """
    __slots__ = ("token",)

    def __init__(self, token="x"):
        self.token = token


class SlottedChild(SlottedParent):
    """Child must call parent's __init__ to initialize the slot. B09."""
    def __init__(self, token="x"):
        ...


# -----------------------------
# B10 — Built-in parent (dict)
# -----------------------------
class ParentBuiltinDict(dict):
    """Built-in dict as a base; expects mapping/iterable. B10."""
    def __init__(self, initial=None):
        super().__init__(initial or {})


class ChildBuiltinDict(ParentBuiltinDict):
    """Quick-fix should insert super().__init__(initial). B10."""
    def __init__(self, initial=None):
        ...


# -----------------------------
# B11 — Built-in parent (set)
# -----------------------------
class ParentBuiltinSet(set):
    """Built-in set as a base; expects iterable. B11."""
    def __init__(self, iterable=()):
        super().__init__(iterable)


class ChildBuiltinSet(ParentBuiltinSet):
    """Quick-fix should insert super().__init__(iterable). B11."""
    def __init__(self, iterable=()):
        ...


# -----------------------------
# B12 — Parent accepts **kwargs only
# -----------------------------
class KwOnlyParent:
    """Parent accepts only **kwargs. B12."""
    def __init__(self, **kwargs):
        ...


class KwOnlyChild(KwOnlyParent):
    """
    Child exposes one kw-only parameter `limit` and collects the rest into **rest.
    Quick-fix should forward only the remainder: super().__init__(**rest). B12.
    """
    def __init__(self, *, limit=100, **rest):
        ...


# -----------------------------
# B13 — Mixed positional-only + keyword-only
# -----------------------------
class MixedKindsParent:
    """Parent mixes (x, /, y, *, flag=False). B13."""
    def __init__(self, x, /, y, *, flag=False):
        ...


class MixedKindsChild(MixedKindsParent):
    """
    Quick-fix must keep kinds: x positionally, y positionally-or-by-name per IDE,
    flag as keyword → super().__init__(x, y, flag=flag). B13.
    """
    def __init__(self, x, /, y, *, flag=False):
        ...


# -----------------------------
# B14 — Abstract Base Class (single inheritance)
# -----------------------------
from abc import ABC


class AbstractParent(ABC):
    """ABC can still define a real __init__ that must be called. B14."""
    def __init__(self, name):
        self._name = name


class AbstractChild(AbstractParent):
    """Quick-fix should insert super().__init__(name). B14."""
    def __init__(self, name):
        ...


# -----------------------------
# B15 — Real-world: threading.Thread
# -----------------------------
import threading


class MyThread(threading.Thread):
    """
    Real parent with many optional args. Quick-fix should build a named call like
    super().__init__(group, target, name, daemon=daemon). B15.
    """
    def __init__(self, group=None, target=None, name=None, daemon=None):
        ...

