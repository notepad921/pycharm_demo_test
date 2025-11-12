
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

class Parent74:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child74(Parent74):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 74

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

class Top77:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left77(Top77):
    def __init__(self, x):
        super().__init__(x)

class Right77(Top77):
    def __init__(self, x):
        super().__init__(x)

class Bottom77(Left77, Right77):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent78:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child78(Parent78):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 78

class Parent79:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child79(Parent79):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 79

class Parent80:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child80(Parent80):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 80

class Parent81:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child81(Parent81):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 81

class Parent82:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child82(Parent82):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 82

class Parent83:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child83(Parent83):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 83

class Top84:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left84(Top84):
    def __init__(self, x):
        super().__init__(x)

class Right84(Top84):
    def __init__(self, x):
        super().__init__(x)

class Bottom84(Left84, Right84):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent85:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child85(Parent85):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 85

class Parent86:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child86(Parent86):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 86

class Parent87:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child87(Parent87):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 87

class Parent88:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child88(Parent88):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 88

class Parent89:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child89(Parent89):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 89

class Parent90:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child90(Parent90):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 90

class Top91:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left91(Top91):
    def __init__(self, x):
        super().__init__(x)

class Right91(Top91):
    def __init__(self, x):
        super().__init__(x)

class Bottom91(Left91, Right91):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent92:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child92(Parent92):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 92

class Parent93:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child93(Parent93):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 93

class Parent94:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child94(Parent94):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 94

class Parent95:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child95(Parent95):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 95

class Parent96:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child96(Parent96):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 96

class Parent97:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child97(Parent97):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 97

class Top98:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left98(Top98):
    def __init__(self, x):
        super().__init__(x)

class Right98(Top98):
    def __init__(self, x):
        super().__init__(x)

class Bottom98(Left98, Right98):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent99:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child99(Parent99):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 99

class Parent100:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child100(Parent100):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 100

class Parent101:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child101(Parent101):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 101

class Parent102:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child102(Parent102):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 102

class Parent103:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child103(Parent103):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 103

class Parent104:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child104(Parent104):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 104

class Top105:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left105(Top105):
    def __init__(self, x):
        super().__init__(x)

class Right105(Top105):
    def __init__(self, x):
        super().__init__(x)

class Bottom105(Left105, Right105):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent106:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child106(Parent106):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 106

class Parent107:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child107(Parent107):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 107

class Parent108:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child108(Parent108):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 108

class Parent109:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child109(Parent109):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 109

class Parent110:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child110(Parent110):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 110

class Parent111:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child111(Parent111):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 111

class Top112:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left112(Top112):
    def __init__(self, x):
        super().__init__(x)

class Right112(Top112):
    def __init__(self, x):
        super().__init__(x)

class Bottom112(Left112, Right112):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent113:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child113(Parent113):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 113

class Parent114:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child114(Parent114):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 114

class Parent115:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child115(Parent115):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 115

class Parent116:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child116(Parent116):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 116

class Parent117:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child117(Parent117):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 117

class Parent118:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child118(Parent118):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 118

class Top119:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left119(Top119):
    def __init__(self, x):
        super().__init__(x)

class Right119(Top119):
    def __init__(self, x):
        super().__init__(x)

class Bottom119(Left119, Right119):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent120:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child120(Parent120):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 120

class Parent121:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child121(Parent121):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 121

class Parent122:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child122(Parent122):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 122

class Parent123:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child123(Parent123):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 123

class Parent124:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child124(Parent124):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 124

class Parent125:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child125(Parent125):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 125

class Top126:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left126(Top126):
    def __init__(self, x):
        super().__init__(x)

class Right126(Top126):
    def __init__(self, x):
        super().__init__(x)

class Bottom126(Left126, Right126):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent127:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child127(Parent127):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 127

class Parent128:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child128(Parent128):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 128

class Parent129:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child129(Parent129):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 129

class Parent130:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child130(Parent130):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 130

class Parent131:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child131(Parent131):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 131

class Parent132:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child132(Parent132):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 132

class Top133:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left133(Top133):
    def __init__(self, x):
        super().__init__(x)

class Right133(Top133):
    def __init__(self, x):
        super().__init__(x)

class Bottom133(Left133, Right133):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent134:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child134(Parent134):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 134

class Parent135:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child135(Parent135):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 135

class Parent136:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child136(Parent136):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 136

class Parent137:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child137(Parent137):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 137

class Parent138:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child138(Parent138):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 138

class Parent139:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child139(Parent139):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 139

class Top140:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left140(Top140):
    def __init__(self, x):
        super().__init__(x)

class Right140(Top140):
    def __init__(self, x):
        super().__init__(x)

class Bottom140(Left140, Right140):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent141:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child141(Parent141):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 141

class Parent142:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child142(Parent142):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 142

class Parent143:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child143(Parent143):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 143

class Parent144:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child144(Parent144):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 144

class Parent145:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child145(Parent145):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 145

class Parent146:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child146(Parent146):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 146

class Top147:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left147(Top147):
    def __init__(self, x):
        super().__init__(x)

class Right147(Top147):
    def __init__(self, x):
        super().__init__(x)

class Bottom147(Left147, Right147):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent148:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child148(Parent148):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 148

class Parent149:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child149(Parent149):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 149

class Parent150:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child150(Parent150):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 150

class Parent151:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child151(Parent151):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 151

class Parent152:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child152(Parent152):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 152

class Parent153:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child153(Parent153):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 153

class Top154:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left154(Top154):
    def __init__(self, x):
        super().__init__(x)

class Right154(Top154):
    def __init__(self, x):
        super().__init__(x)

class Bottom154(Left154, Right154):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent155:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child155(Parent155):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 155

class Parent156:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child156(Parent156):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 156

class Parent157:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child157(Parent157):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 157

class Parent158:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child158(Parent158):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 158

class Parent159:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child159(Parent159):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 159

class Parent160:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child160(Parent160):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 160

class Top161:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left161(Top161):
    def __init__(self, x):
        super().__init__(x)

class Right161(Top161):
    def __init__(self, x):
        super().__init__(x)

class Bottom161(Left161, Right161):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent162:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child162(Parent162):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 162

class Parent163:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child163(Parent163):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 163

class Parent164:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child164(Parent164):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 164

class Parent165:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child165(Parent165):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 165

class Parent166:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child166(Parent166):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 166

class Parent167:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child167(Parent167):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 167

class Top168:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left168(Top168):
    def __init__(self, x):
        super().__init__(x)

class Right168(Top168):
    def __init__(self, x):
        super().__init__(x)

class Bottom168(Left168, Right168):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent169:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child169(Parent169):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 169

class Parent170:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child170(Parent170):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 170

class Parent171:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child171(Parent171):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 171

class Parent172:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child172(Parent172):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 172

class Parent173:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child173(Parent173):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 173

class Parent174:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child174(Parent174):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 174

class Top175:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left175(Top175):
    def __init__(self, x):
        super().__init__(x)

class Right175(Top175):
    def __init__(self, x):
        super().__init__(x)

class Bottom175(Left175, Right175):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent176:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child176(Parent176):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 176

class Parent177:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child177(Parent177):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 177

class Parent178:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child178(Parent178):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 178

class Parent179:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child179(Parent179):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 179

class Parent180:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child180(Parent180):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 180

class Parent181:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child181(Parent181):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 181

class Top182:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left182(Top182):
    def __init__(self, x):
        super().__init__(x)

class Right182(Top182):
    def __init__(self, x):
        super().__init__(x)

class Bottom182(Left182, Right182):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent183:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child183(Parent183):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 183

class Parent184:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child184(Parent184):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 184

class Parent185:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child185(Parent185):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 185

class Parent186:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child186(Parent186):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 186

class Parent187:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child187(Parent187):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 187

class Parent188:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child188(Parent188):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 188

class Top189:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left189(Top189):
    def __init__(self, x):
        super().__init__(x)

class Right189(Top189):
    def __init__(self, x):
        super().__init__(x)

class Bottom189(Left189, Right189):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent190:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child190(Parent190):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 190

class Parent191:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child191(Parent191):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 191

class Parent192:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child192(Parent192):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 192

class Parent193:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child193(Parent193):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 193

class Parent194:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child194(Parent194):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 194

class Parent195:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child195(Parent195):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 195

class Top196:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left196(Top196):
    def __init__(self, x):
        super().__init__(x)

class Right196(Top196):
    def __init__(self, x):
        super().__init__(x)

class Bottom196(Left196, Right196):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent197:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child197(Parent197):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 197

class Parent198:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child198(Parent198):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 198

class Parent199:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child199(Parent199):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 199

class Parent200:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child200(Parent200):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 200

class Parent201:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child201(Parent201):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 201

class Parent202:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child202(Parent202):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 202

class Top203:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left203(Top203):
    def __init__(self, x):
        super().__init__(x)

class Right203(Top203):
    def __init__(self, x):
        super().__init__(x)

class Bottom203(Left203, Right203):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent204:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child204(Parent204):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 204

class Parent205:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child205(Parent205):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 205

class Parent206:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child206(Parent206):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 206

class Parent207:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child207(Parent207):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 207

class Parent208:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child208(Parent208):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 208

class Parent209:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child209(Parent209):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 209

class Top210:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left210(Top210):
    def __init__(self, x):
        super().__init__(x)

class Right210(Top210):
    def __init__(self, x):
        super().__init__(x)

class Bottom210(Left210, Right210):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent211:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child211(Parent211):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 211

class Parent212:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child212(Parent212):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 212

class Parent213:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child213(Parent213):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 213

class Parent214:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child214(Parent214):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 214

class Parent215:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child215(Parent215):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 215

class Parent216:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child216(Parent216):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 216

class Top217:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left217(Top217):
    def __init__(self, x):
        super().__init__(x)

class Right217(Top217):
    def __init__(self, x):
        super().__init__(x)

class Bottom217(Left217, Right217):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent218:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child218(Parent218):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 218

class Parent219:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child219(Parent219):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 219

class Parent220:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child220(Parent220):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 220

class Parent221:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child221(Parent221):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 221

class Parent222:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child222(Parent222):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 222

class Parent223:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child223(Parent223):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 223

class Top224:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left224(Top224):
    def __init__(self, x):
        super().__init__(x)

class Right224(Top224):
    def __init__(self, x):
        super().__init__(x)

class Bottom224(Left224, Right224):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent225:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child225(Parent225):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 225

class Parent226:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child226(Parent226):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 226

class Parent227:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child227(Parent227):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 227

class Parent228:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child228(Parent228):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 228

class Parent229:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child229(Parent229):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 229

class Parent230:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child230(Parent230):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 230

class Top231:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left231(Top231):
    def __init__(self, x):
        super().__init__(x)

class Right231(Top231):
    def __init__(self, x):
        super().__init__(x)

class Bottom231(Left231, Right231):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent232:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child232(Parent232):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 232

class Parent233:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child233(Parent233):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 233

class Parent234:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child234(Parent234):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 234

class Parent235:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child235(Parent235):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 235

class Parent236:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child236(Parent236):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 236

class Parent237:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child237(Parent237):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 237

class Top238:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left238(Top238):
    def __init__(self, x):
        super().__init__(x)

class Right238(Top238):
    def __init__(self, x):
        super().__init__(x)

class Bottom238(Left238, Right238):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent239:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child239(Parent239):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 239

class Parent240:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child240(Parent240):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 240

class Parent241:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child241(Parent241):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 241

class Parent242:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child242(Parent242):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 242

class Parent243:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child243(Parent243):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 243

class Parent244:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child244(Parent244):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 244

class Top245:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left245(Top245):
    def __init__(self, x):
        super().__init__(x)

class Right245(Top245):
    def __init__(self, x):
        super().__init__(x)

class Bottom245(Left245, Right245):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent246:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child246(Parent246):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 246

class Parent247:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child247(Parent247):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 247

class Parent248:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child248(Parent248):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 248

class Parent249:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child249(Parent249):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 249

class Parent250:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child250(Parent250):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 250

class Parent251:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child251(Parent251):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 251

class Top252:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left252(Top252):
    def __init__(self, x):
        super().__init__(x)

class Right252(Top252):
    def __init__(self, x):
        super().__init__(x)

class Bottom252(Left252, Right252):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent253:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child253(Parent253):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 253

class Parent254:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child254(Parent254):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 254

class Parent255:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child255(Parent255):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 255

class Parent256:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child256(Parent256):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 256

class Parent257:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child257(Parent257):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 257

class Parent258:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child258(Parent258):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 258

class Top259:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left259(Top259):
    def __init__(self, x):
        super().__init__(x)

class Right259(Top259):
    def __init__(self, x):
        super().__init__(x)

class Bottom259(Left259, Right259):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent260:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child260(Parent260):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 260

class Parent261:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child261(Parent261):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 261

class Parent262:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child262(Parent262):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 262

class Parent263:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child263(Parent263):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 263

class Parent264:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child264(Parent264):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 264

class Parent265:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child265(Parent265):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 265

class Top266:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left266(Top266):
    def __init__(self, x):
        super().__init__(x)

class Right266(Top266):
    def __init__(self, x):
        super().__init__(x)

class Bottom266(Left266, Right266):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent267:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child267(Parent267):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 267

class Parent268:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child268(Parent268):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 268

class Parent269:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child269(Parent269):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 269

class Parent270:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child270(Parent270):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 270

class Parent271:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child271(Parent271):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 271

class Parent272:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child272(Parent272):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 272

class Top273:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left273(Top273):
    def __init__(self, x):
        super().__init__(x)

class Right273(Top273):
    def __init__(self, x):
        super().__init__(x)

class Bottom273(Left273, Right273):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent274:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child274(Parent274):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 274

class Parent275:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child275(Parent275):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 275

class Parent276:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child276(Parent276):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 276

class Parent277:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child277(Parent277):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 277

class Parent278:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child278(Parent278):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 278

class Parent279:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child279(Parent279):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 279

class Top280:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left280(Top280):
    def __init__(self, x):
        super().__init__(x)

class Right280(Top280):
    def __init__(self, x):
        super().__init__(x)

class Bottom280(Left280, Right280):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent281:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child281(Parent281):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 281

class Parent282:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child282(Parent282):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 282

class Parent283:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child283(Parent283):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 283

class Parent284:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child284(Parent284):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 284

class Parent285:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child285(Parent285):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 285

class Parent286:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child286(Parent286):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 286

class Top287:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left287(Top287):
    def __init__(self, x):
        super().__init__(x)

class Right287(Top287):
    def __init__(self, x):
        super().__init__(x)

class Bottom287(Left287, Right287):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent288:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child288(Parent288):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 288

class Parent289:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child289(Parent289):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 289

class Parent290:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child290(Parent290):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 290

class Parent291:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child291(Parent291):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 291

class Parent292:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child292(Parent292):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 292

class Parent293:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child293(Parent293):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 293

class Top294:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left294(Top294):
    def __init__(self, x):
        super().__init__(x)

class Right294(Top294):
    def __init__(self, x):
        super().__init__(x)

class Bottom294(Left294, Right294):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent295:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child295(Parent295):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 295

class Parent296:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child296(Parent296):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 296

class Parent297:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child297(Parent297):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 297

class Parent298:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child298(Parent298):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 298

class Parent299:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child299(Parent299):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 299

class Parent300:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child300(Parent300):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 300

class Top301:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left301(Top301):
    def __init__(self, x):
        super().__init__(x)

class Right301(Top301):
    def __init__(self, x):
        super().__init__(x)

class Bottom301(Left301, Right301):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent302:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child302(Parent302):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 302

class Parent303:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child303(Parent303):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 303

class Parent304:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child304(Parent304):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 304

class Parent305:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child305(Parent305):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 305

class Parent306:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child306(Parent306):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 306

class Parent307:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child307(Parent307):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 307

class Top308:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left308(Top308):
    def __init__(self, x):
        super().__init__(x)

class Right308(Top308):
    def __init__(self, x):
        super().__init__(x)

class Bottom308(Left308, Right308):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent309:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child309(Parent309):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 309

class Parent310:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child310(Parent310):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 310

class Parent311:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child311(Parent311):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 311

class Parent312:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child312(Parent312):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 312

class Parent313:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child313(Parent313):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 313

class Parent314:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child314(Parent314):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 314

class Top315:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left315(Top315):
    def __init__(self, x):
        super().__init__(x)

class Right315(Top315):
    def __init__(self, x):
        super().__init__(x)

class Bottom315(Left315, Right315):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent316:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child316(Parent316):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 316

class Parent317:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child317(Parent317):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 317

class Parent318:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child318(Parent318):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 318

class Parent319:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child319(Parent319):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 319

class Parent320:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child320(Parent320):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 320

class Parent321:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child321(Parent321):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 321

class Top322:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left322(Top322):
    def __init__(self, x):
        super().__init__(x)

class Right322(Top322):
    def __init__(self, x):
        super().__init__(x)

class Bottom322(Left322, Right322):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent323:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child323(Parent323):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 323

class Parent324:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child324(Parent324):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 324

class Parent325:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child325(Parent325):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 325

class Parent326:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child326(Parent326):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 326

class Parent327:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child327(Parent327):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 327

class Parent328:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child328(Parent328):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 328

class Top329:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left329(Top329):
    def __init__(self, x):
        super().__init__(x)

class Right329(Top329):
    def __init__(self, x):
        super().__init__(x)

class Bottom329(Left329, Right329):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent330:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child330(Parent330):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 330

class Parent331:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child331(Parent331):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 331

class Parent332:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child332(Parent332):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 332

class Parent333:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child333(Parent333):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 333

class Parent334:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child334(Parent334):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 334

class Parent335:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child335(Parent335):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 335

class Top336:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left336(Top336):
    def __init__(self, x):
        super().__init__(x)

class Right336(Top336):
    def __init__(self, x):
        super().__init__(x)

class Bottom336(Left336, Right336):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent337:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child337(Parent337):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 337

class Parent338:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child338(Parent338):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 338

class Parent339:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child339(Parent339):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 339

class Parent340:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child340(Parent340):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 340

class Parent341:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child341(Parent341):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 341

class Parent342:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child342(Parent342):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 342

class Top343:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left343(Top343):
    def __init__(self, x):
        super().__init__(x)

class Right343(Top343):
    def __init__(self, x):
        super().__init__(x)

class Bottom343(Left343, Right343):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent344:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child344(Parent344):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 344

class Parent345:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child345(Parent345):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 345

class Parent346:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child346(Parent346):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 346

class Parent347:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child347(Parent347):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 347

class Parent348:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child348(Parent348):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 348

class Parent349:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child349(Parent349):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 349

class Top350:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left350(Top350):
    def __init__(self, x):
        super().__init__(x)

class Right350(Top350):
    def __init__(self, x):
        super().__init__(x)

class Bottom350(Left350, Right350):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent351:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child351(Parent351):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 351

class Parent352:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child352(Parent352):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 352

class Parent353:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child353(Parent353):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 353

class Parent354:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child354(Parent354):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 354

class Parent355:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child355(Parent355):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 355

class Parent356:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child356(Parent356):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 356

class Top357:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left357(Top357):
    def __init__(self, x):
        super().__init__(x)

class Right357(Top357):
    def __init__(self, x):
        super().__init__(x)

class Bottom357(Left357, Right357):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent358:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child358(Parent358):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 358

class Parent359:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child359(Parent359):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 359

class Parent360:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child360(Parent360):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 360

class Parent361:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child361(Parent361):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 361

class Parent362:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child362(Parent362):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 362

class Parent363:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child363(Parent363):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 363

class Top364:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left364(Top364):
    def __init__(self, x):
        super().__init__(x)

class Right364(Top364):
    def __init__(self, x):
        super().__init__(x)

class Bottom364(Left364, Right364):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent365:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child365(Parent365):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 365

class Parent366:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child366(Parent366):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 366

class Parent367:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child367(Parent367):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 367

class Parent368:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child368(Parent368):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 368

class Parent369:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child369(Parent369):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 369

class Parent370:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child370(Parent370):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 370

class Top371:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left371(Top371):
    def __init__(self, x):
        super().__init__(x)

class Right371(Top371):
    def __init__(self, x):
        super().__init__(x)

class Bottom371(Left371, Right371):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent372:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child372(Parent372):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 372

class Parent373:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child373(Parent373):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 373

class Parent374:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child374(Parent374):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 374

class Parent375:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child375(Parent375):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 375

class Parent376:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child376(Parent376):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 376

class Parent377:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child377(Parent377):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 377

class Top378:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left378(Top378):
    def __init__(self, x):
        super().__init__(x)

class Right378(Top378):
    def __init__(self, x):
        super().__init__(x)

class Bottom378(Left378, Right378):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent379:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child379(Parent379):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 379

class Parent380:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child380(Parent380):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 380

class Parent381:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child381(Parent381):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 381

class Top382:
    """Top of diamond."""
    def __init__(self, x):
        self.x = x

class Left382(Top382):
    def __init__(self, x):
        super().__init__(x)

class Right382(Top382):
    def __init__(self, x):
        super().__init__(x)

class Bottom382(Left382, Right382):
    """Expected: cooperative super().__init__(x), not a direct Top call."""
    def __init__(self, x):
        # super() must be inserted here
        self.x_snapshot = x

class Parent383:
    """Trivial init; sets a readiness flag."""
    def __init__(self):
        self.ready = True

class Child383(Parent383):
    """Expected: insert super().__init__() BEFORE early reliance on parent state."""
    def __init__(self):
        # EARLY RELIANCE: must be after super().__init__()
        self.parent_ready_snapshot = self.ready
        self.marker = 383
