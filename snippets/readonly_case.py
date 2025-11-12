"""
Read-only check.

Windows:
    attrib +R snippets\\readonly_case.py
    attrib -R snippets\\readonly_case.py

POSIX:
    chmod a-w snippets/readonly_case.py
    chmod u+w snippets/readonly_case.py
"""

# -----------------------------
# R01 — Quick-fix availability in read-only files
# -----------------------------


class ROParent:
    def __init__(self, token="x"):
        self.token = token

class ROChild(ROParent):
    """Expected: The inspection works, but the IDE explicitly shows that the quick-fix cannot be applied
     because of RO. R01."""
    def __init__(self, token="x"):
        ...
