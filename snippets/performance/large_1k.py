"""
Performance scenario for the quick-fix.
# P01 — 1k parent/child pairs mixed with diamonds to check batch fixes.
"""

class Parent1:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child1(Parent1):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 1

class Parent2:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child2(Parent2):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 2

class Parent3:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child3(Parent3):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 3

class Parent4:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child4(Parent4):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 4

class Parent5:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child5(Parent5):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 5

class Parent6:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child6(Parent6):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 6

class Top7:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left7(Top7):
    def __init__(self, x):
        super().__init__(x)

class Right7(Top7):
    def __init__(self, x):
        super().__init__(x)

class Bottom7(Left7, Right7):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent8:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child8(Parent8):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 8

class Parent9:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child9(Parent9):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 9

class Parent10:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child10(Parent10):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 10

class Parent11:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child11(Parent11):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 11

class Parent12:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child12(Parent12):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 12

class Parent13:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child13(Parent13):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 13

class Top14:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left14(Top14):
    def __init__(self, x):
        super().__init__(x)

class Right14(Top14):
    def __init__(self, x):
        super().__init__(x)

class Bottom14(Left14, Right14):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent15:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child15(Parent15):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 15

class Parent16:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child16(Parent16):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 16

class Parent17:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child17(Parent17):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 17

class Parent18:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child18(Parent18):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 18

class Parent19:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child19(Parent19):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 19

class Parent20:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child20(Parent20):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 20

class Top21:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left21(Top21):
    def __init__(self, x):
        super().__init__(x)

class Right21(Top21):
    def __init__(self, x):
        super().__init__(x)

class Bottom21(Left21, Right21):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent22:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child22(Parent22):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 22

class Parent23:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child23(Parent23):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 23

class Parent24:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child24(Parent24):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 24

class Parent25:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child25(Parent25):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 25

class Parent26:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child26(Parent26):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 26

class Parent27:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child27(Parent27):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 27

class Top28:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left28(Top28):
    def __init__(self, x):
        super().__init__(x)

class Right28(Top28):
    def __init__(self, x):
        super().__init__(x)

class Bottom28(Left28, Right28):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent29:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child29(Parent29):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 29

class Parent30:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child30(Parent30):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 30

class Parent31:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child31(Parent31):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 31

class Parent32:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child32(Parent32):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 32

class Parent33:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child33(Parent33):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 33

class Parent34:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child34(Parent34):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 34

class Top35:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left35(Top35):
    def __init__(self, x):
        super().__init__(x)

class Right35(Top35):
    def __init__(self, x):
        super().__init__(x)

class Bottom35(Left35, Right35):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent36:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child36(Parent36):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 36

class Parent37:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child37(Parent37):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 37

class Parent38:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child38(Parent38):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 38

class Parent39:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child39(Parent39):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 39

class Parent40:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child40(Parent40):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 40

class Parent41:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child41(Parent41):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 41

class Top42:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left42(Top42):
    def __init__(self, x):
        super().__init__(x)

class Right42(Top42):
    def __init__(self, x):
        super().__init__(x)

class Bottom42(Left42, Right42):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent43:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child43(Parent43):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 43

class Parent44:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child44(Parent44):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 44

class Parent45:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child45(Parent45):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 45

class Parent46:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child46(Parent46):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 46

class Parent47:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child47(Parent47):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 47

class Parent48:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child48(Parent48):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 48

class Top49:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left49(Top49):
    def __init__(self, x):
        super().__init__(x)

class Right49(Top49):
    def __init__(self, x):
        super().__init__(x)

class Bottom49(Left49, Right49):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent50:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child50(Parent50):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 50

class Parent51:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child51(Parent51):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 51

class Parent52:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child52(Parent52):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 52

class Parent53:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child53(Parent53):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 53

class Parent54:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child54(Parent54):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 54

class Parent55:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child55(Parent55):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 55

class Top56:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left56(Top56):
    def __init__(self, x):
        super().__init__(x)

class Right56(Top56):
    def __init__(self, x):
        super().__init__(x)

class Bottom56(Left56, Right56):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent57:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child57(Parent57):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 57

class Parent58:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child58(Parent58):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 58

class Parent59:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child59(Parent59):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 59

class Parent60:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child60(Parent60):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 60

class Parent61:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child61(Parent61):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 61

class Parent62:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child62(Parent62):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 62

class Top63:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left63(Top63):
    def __init__(self, x):
        super().__init__(x)

class Right63(Top63):
    def __init__(self, x):
        super().__init__(x)

class Bottom63(Left63, Right63):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent64:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child64(Parent64):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 64

class Parent65:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child65(Parent65):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 65

class Parent66:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child66(Parent66):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 66

class Parent67:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child67(Parent67):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 67

class Parent68:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child68(Parent68):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 68

class Parent69:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child69(Parent69):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 69

class Top70:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left70(Top70):
    def __init__(self, x):
        super().__init__(x)

class Right70(Top70):
    def __init__(self, x):
        super().__init__(x)

class Bottom70(Left70, Right70):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent71:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child71(Parent71):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 71

class Parent72:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child72(Parent72):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 72

class Parent73:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child73(Parent73):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 73

class Top74:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left74(Top74):
    def __init__(self, x):
        super().__init__(x)

class Right74(Top74):
    def __init__(self, x):
        super().__init__(x)

class Bottom74(Left74, Right74):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent75:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child75(Parent75):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 75

class Parent76:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child76(Parent76):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 76
