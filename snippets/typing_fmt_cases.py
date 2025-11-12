"""
Typing & formatting scenarios: docstring placement, long signatures with wrapping
and trailing commas, and defaults. Ensures quick-fix does not break formatting
and keeps docstring as the first statement.
"""

# T01 — Docstring first
class PathParent:
    """Parent requires `path: str`. Used by T01."""
    def __init__(self, path: str):
        ...


class PathChild(PathParent):
    """
    Child must call super().__init__(path) AFTER the docstring. T01.
    The docstring must remain the first statement in the body.
    """
    def __init__(self, path: str):
        """Loads things."""
        ...


# T02 — Long signature, wrapping
class LongSigParent:
    """Parent: long parameter + kw-only flag. Used by T02."""
    def __init__(self, very_looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong_argument_name: str, *, flag: bool = False):
        ...


class LongSigChild(LongSigParent):
    """
    Child must preserve wrapping and trailing comma on insertion.
    The call may be split into lines. T02.
    """
    def __init__(self,
                 very_looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong_argument_name: str, *,
                 flag: bool = False):
        ...


# -----------------------------
# T03 — Multiline docstring (Google/Numpy style)
# -----------------------------
class DocParent:
    """Parent requires x."""
    def __init__(self, x):
        ...


class DocChild(DocParent):
    """
    Quick-fix must insert the call after this multiline docstring
    and must not reflow or rewrap it. T03.
    """
    def __init__(self, x):
        """Summary.

        Args:
            x: Input value.
        """
        ...


# -----------------------------
# T04 — Comments around insertion point
# -----------------------------
class CommentedParent:
    """Parent requires x."""
    def __init__(self, x):
        ...


class CommentedChild(CommentedParent):
    """
    Quick-fix must keep comments intact, inserting the call between them
    without changing spacing/indent. T04.
    """
    def __init__(self, x):
        # prepare something
        ...
        # finalize
