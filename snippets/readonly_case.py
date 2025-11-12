"""
Read-only safety check.

Windows:
    attrib +R snippets\\readonly_case.py
    attrib -R snippets\\readonly_case.py

POSIX:
    chmod a-w snippets/readonly_case.py
    chmod u+w snippets/readonly_case.py
"""

class ROParent:
    def __init__(self, token="x"):
        self.token = token

class ROChild(ROParent):
    """Expected: IDE  doesn't raise an inspection, and does not offer the quick-fix in RO mode"""
    def __init__(self, token="x"):
        ...
