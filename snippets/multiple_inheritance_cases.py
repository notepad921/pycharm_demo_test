# M01 — Diamond, cooperative
class DiamondTopParent:
    def __init__(self, x): ...


class DiamondMixinCooperative:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DiamondChild(DiamondTopParent, DiamondMixinCooperative):
    def __init__(self, x):
        ...


# M02 — Mixin without __init__
class MixinNoInit:
    pass


class MixBaseWithInit:
    def __init__(self, x): ...


class MixChild(MixinNoInit, MixBaseWithInit):
    def __init__(self, x):
        ...


# M03 — Base without __init__
class EmptyBaseNoInit:
    pass


class ChildOverEmptyBase(EmptyBaseNoInit):
    def __init__(self):
        ...


# M04 — Explicit parent call already present
class ExplicitBase:
    def __init__(self, x): ...


class ExplicitChild(ExplicitBase):
    def __init__(self, x):
        ExplicitBase.__init__(self, x)
