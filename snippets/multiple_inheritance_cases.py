"""Multiple inheritance scenarios for the 'Add superclass call' quick-fix."""


# M01 — Diamond, cooperative
class DiamondTopParent:
    """Top of the diamond; defines __init__(x) """
    def __init__(self, x):
        self.x = x

class DiamondLeft(DiamondTopParent):
    """Left branch cooperatively calls super().__init__(x)."""
    def __init__(self, x):
        super().__init__(x)


class DiamondRight(DiamondTopParent):
    """Right branch is also cooperative via super().__init__(*args, **kwargs)."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiamondChild(DiamondLeft, DiamondRight):
    """Child should call super().__init__(x) to keep the cooperative chain."""
    def __init__(self, x):
        ...


# M02 — Mixin without __init__
class MixinNoInit:
    """Mixin without its own __init__."""
    pass


class MixBaseWithInit:
    """Concrete base defines __init__(x)."""
    def __init__(self, x):
        self.x = x

class MixChild(MixinNoInit, MixBaseWithInit):
    """Quick-fix should insert cooperative super().__init__(x)."""
    def __init__(self, x):
        ...


# M03 — Base without __init__
class EmptyBaseNoInit:
    """Base lacks __init__; inspection should stay quiet."""
    pass


class ChildOverEmptyBase(EmptyBaseNoInit):
    """Child defines __init__ but should not trigger inspection/quick-fix."""
    def __init__(self):
        ...


# M04 — Explicit parent call already present
class ExplicitBase:
    """Base defines __init__(x); child already calls it explicitly. M04."""
    def __init__(self, x):
        self.x = x

class ExplicitChild(ExplicitBase):
    """Explicit base call present → inspection must stay silent (M04)."""
    def __init__(self, x):
        ExplicitBase.__init__(self, x)
