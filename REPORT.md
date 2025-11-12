# Test Report — PyCharm Quick-Fix “Add superclass call” (Inspection + Quick-Fix)

**Goal**  
Verify that when a subclass defines `__init__` and omits the parent’s constructor call, PyCharm:  
(a) raises an inspection, and (b) offers & applies the quick-fix that inserts `super().__init__(...)` correctly without breaking formatting or semantics.

**Environment**  
- OS: Windows 11 Home (Windows 11.0)  
- PyCharm: PyCharm 2025.2.4
Build #PY-252.27397.106, built on October 23, 2025
Source revision: 7bc036de6fb8a
Runtime version: 21.0.8+1-b1038.73 amd64 (JCEF 122.1.9)
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Toolkit: sun.awt.windows.WToolkit
GC: G1 Young Generation, G1 Concurrent GC, G1 Old Generation
Memory: 2048M
Cores: 16
Registry:
  ide.experimental.ui=true
Non-Bundled Plugins:
  Docker (252.27397.129)

- Python: 3.13.x  
- Scope: We test this *feature pair* (inspection + quick-fix).
- Out of scope → global inspection settings, profiles, automation, deep performance testing, localization, usability testing.

**Status legend:** PASS / ❌ FAIL

For **❌ FAIL** I include a block with unexpected code after applying this quick-fix.

---

## B01 — Single inheritance, no args
**Snippet:** `snippets/basic_cases.py` (B01, B01a)  
**Steps:** Place caret on `ChildNoArgs.__init__` → Alt+Enter → *Add superclass call*.  
**Expected result:** Child inserts `super().__init__()`; formatting intact; earlier code is not allowed to rely on parent state before the call.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B02 — Positional + default
**Snippet:** `snippets/basic_cases.py` (B02)  
**Expected result:** Insert `super().__init__(x, y)` before `self.y = y`; formatting unchanged.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B03 — Keyword-only
**Snippet:** `snippets/basic_cases.py` (B03)  
**Expected result:** Insert `super().__init__(limit=limit)` after the docstring; the docstring remains the first statement.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B04 — Positional-only (PEP 570)
**Snippet:** `snippets/basic_cases.py` (B04)  
**Expected result:** Pass `x` positionally and not by name; insert `super().__init__(x, y)`.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## B05 — Varargs passthrough
**Snippet:** `snippets/basic_cases.py` (B05)  
**Expected result:** Forward only the variable arguments to the parent using `super().__init__(*args, **kwargs)` and do not pass the child-only parameter.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B06 — Param names differ
**Snippet:** `snippets/basic_cases.py` (B06)  
**Expected result:** “Match identical names and pass them by keyword. Do not forward **remaining_kwargs because the parent does not accept it. Do not guess uid → user_id.”

**Actual:**  exactly as expected

**Status:**  PASS

```  incorrect code after applying  
```

## B07 — Built-in parent (list)
**Snippet:** `snippets/basic_cases.py` (B07)  
**Expected result:** Insert `super().__init__(iterable)` and preserve layout despite a C-implemented base.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```


## B08 — Parent uses __slots__
**Snippet:** `snippets/basic_cases.py` (B08)  
**Expected result:** Insert a parent call (e.g., `super().__init__(token=token)`) so that slot-backed attributes are initialized; formatting remains intact.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B10 — Built-in parent (dict)
**Snippet:** `snippets/basic_cases.py` (B10)  
**Expected result:** Insert `super().__init__(initial)` and keep indentation and spacing unchanged.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B11 — Built-in parent (set)
**Snippet:** `snippets/basic_cases.py` (B11)  
**Expected result:** Insert `super().__init__(iterable)` without formatting changes.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B12 — Parent accepts **kwargs only
**Snippet:** `snippets/basic_cases.py` (B12)  
**Expected result:** Forward the remaining named arguments via `super().__init__(**rest)` and keep child-only parameters local.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B13 — Mixed positional-only + keyword-only
**Snippet:** `snippets/basic_cases.py` (B13)  
**Expected result:** Preserve argument kinds by passing positional-only arguments positionally and keyword-only by name, e.g., `super().__init__(x, y, flag=flag)`.  

**Actual:**  super().__init__(x, y, flag=flag) is ok, but extra "/" was added to child args (it's another quick-fix, not our target, just light the problem)

**Status:** PASS, but another quick-fix ❌ FAIL, just FYI

```    
def __init__(self, x, /, y, /, *, flag=False): <---- extra "/" was added here, syntax error!
    super().__init__(x, y, flag=flag)
    ...
```

## B14 — Abstract Base Class (ABC)
**Snippet:** `snippets/basic_cases.py` (B14)  
**Expected result:** Insert `super().__init__(name)`; abstractness does not change call requirements.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## B15 — Standard library class — threading.Thread
**Snippet:** `snippets/basic_cases.py` (B15)  
**Expected result:** Build a keyworded call reflecting provided arguments, e.g., `super().__init__(group, target, name, daemon=daemon)`; preserve formatting.  
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```


## B16 — Single inheritance, by mouse click
**Snippet:** `snippets/basic_cases.py` (B01)  
**Steps:** Place a mouse on `ChildNoArgs.__init__` → left click → *Add superclass call*.  
**Expected result:** Child inserts `super().__init__()`; formatting intact;
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```

## B17 — Single inheritance, quick-fix, than UNDO and REDO
**Snippet:** `snippets/basic_cases.py` (B01)  
**Steps:** Place caret on `ChildNoArgs.__init__` → Alt+Enter → *Add superclass call* → ctrl-Z → ctrl-shift-Z.  
**Expected result:** Child inserts `super().__init__()`; formatting intact; applying of the fix is first canceled, then returned.
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```
---

## M01 — Diamond, cooperative
**Snippet:** `snippets/multiple_inheritance_cases.py` (M01)  
**Expected result:** Prefer a cooperative `super().__init__(x)` call rather than addressing a specific base directly.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## M02 — Mixin without __init__
**Snippet:** `snippets/multiple_inheritance_cases.py` (M02)  
**Expected result:** Offer the quick-fix and insert `super().__init__(x)` according to MRO even if one of the bases has no `__init__`.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## M03 — Base without __init__
**Snippet:** `snippets/multiple_inheritance_cases.py` (M03)  
**Expected result:** Do not raise an inspection and do not offer a quick-fix when the nearest MRO parents do not define `__init__`.  
**Actual:**  exactly as expected

**Status:**  PASS

```incorrect code after applying
```

## M04 — Explicit parent call already present
**Snippet:** `snippets/multiple_inheritance_cases.py` (M04)  
**Expected result:** Stay silent (no inspection, no quick-fix) when the child already calls a parent initializer explicitly.  
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```

---

## D01 — Parent is @dataclass
**Snippet:** `snippets/dataclasses_cases.py` (D01)  
**Expected result:** Construct a keyworded call to the dataclass parent initializer, e.g., `super().__init__(id=id, name=name)`; keep any docstring first.  
**Actual:**  The inspector does not indicate that a fix needs to be called.

**Status:**  ❌ FAIL

```
no code changing
```

## D02 — Child is @dataclass (auto-generated __init__)
**Snippet:** `snippets/dataclasses_cases.py` (D02)  
**Expected result:** Do not show the inspection when the child relies on the dataclass-generated `__init__`.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## D03 — Dataclass parent kw_only=True
**Snippet:** `snippets/dataclasses_cases.py` (D03)  
**Expected result:** Use a keyworded call to respect keyword-only dataclass fields, e.g., `super().__init__(id=id, name=name)`; no positional passing.  
**Actual:**  The inspector does not indicate that a fix needs to be called.
**Status:**  ❌ FAIL

```
no code changing
```

---

## T01 — Docstring first
**Snippet:** `snippets/typing_fmt_cases.py` (T01)  
**Expected result:** Place the inserted call immediately after the docstring without reflowing it.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## T02 — Long signature, wrapping
**Snippet:** `snippets/typing_fmt_cases.py` (T02)  
**Expected result:** Preserve multi-line wrapping and trailing comma in the signature and body; the inserted call may be multi-line but must not reformat the function.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```


## T03 — Multiline docstring (Google/Numpy)
**Snippet:** `snippets/typing_fmt_cases.py` (T03)  
**Expected result:** Insert the call after the multiline docstring block and do not modify docstring formatting.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## T04 — Comments around insertion point
**Snippet:** `snippets/typing_fmt_cases.py` (T04)  
**Expected result:** Keep surrounding comments intact and insert the call between them without altering spacing.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

---

## E01 — Wrong decorators
**Snippet:** `snippets/edge_cases.py` (E01)  
**Expected result:** Do not offer a quick-fix when `__init__` is decorated incorrectly (e.g., `@staticmethod`).  
**Actual:**  inspector propose to add super().__init__(), it could be done

**Status:**  ❌ FAILED

```
class DecorChild(DecorParent):
    """
    @staticmethod on __init__ is semantically invalid; inspection should not
    propose 'Add superclass call'. E01.
    """
    @staticmethod
    def __init__(self):
        super().__init__() <--- added
        ...
```

## E02 — super in try/except
**Snippet:** `snippets/edge_cases.py` (E02)  
**Expected result:** Do not raise an inspection when a `super()` call already exists inside a `try/except` block.  
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```

## E03 — Metaclass / __new__
**Snippet:** `snippets/edge_cases.py` (E03)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the parent defines only `__new__` and no `__init__`.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## E04 — Parent is object
**Snippet:** `snippets/edge_cases.py` (E04)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the only parent is `object`.  
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```

## E05 — Parent defines __init__ = object.__init__
**Snippet:** `snippets/edge_cases.py` (E05)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the parent explicitly aliases `__init__` to `object.__init__`.  
**Actual:**  exactly as expected

**Status:**  PASS 

```incorrect code after applying
```

## E06 — Conditional super() already present
**Snippet:** `snippets/edge_cases.py` (E06)  
**Expected result:** Do not raise an inspection when a `super()` call is already present under a condition.  
**Actual:**  exactly as expected

**Status:**  PASS  

```incorrect code after applying
```

## R01 — Read-only file should support inspection
**Snippet:** `snippets/readonly_case.py` (R01)

**Expected result:** The inspection should work, IDE should display an explicit warning that the quick fix cannot be applied because the file is not available for editing.

**Actual:**  The inspection does not work, the user does not see an error in the code for no explicit reason.

**Status:**  ❌ FAIL



## P01 — 1k lines file bulk edit scenario
**Snippet:** `snippets/performance/large_1k.py` (P01)

**Expected result:** The inspection and quick-fix remain responsive when scanning or applying bulk changes across ~1k affected lines (76 places) in a file in 3 seconds.

I don't have any statistics or numbers to reference, so I'm using data from my own user experience for this smoke performance test. True performance testing is out of scope.

**Actual:** ~2.7 seconds in 10 runs

**Status:** PASS  



## P02 — 5k lines file bulk edit scenario
**Snippet:** `snippets/performance/large_5k.py` (P02)

**Expected result:** Even with ~5k affected lines (383 places), PyCharm should keep the UI responsive and finish applying the bulk quick-fix in 15 seconds.

It should be completed within a reasonable time frame. I don't have any statistics or numbers to reference, so I'm using data from my own user experience for this smoke performance test. True performance testing is out of scope.

**Actual:** ~32.1 seconds in 10 runs. The execution speed increases non-linearly; with large numbers of modified classes, the speed is low.

**Status:** ❌ FAIL


## P03 — Small file single quick-fix scenario
**Snippet:** `snippets/basic_cases.py` (B01)  

**Expected result:** Quick-fix is done in <300 ms.

**Actual:**  exactly as expected

**Status:**  PASS 



## P04 — 1k lines file single quick-fix scenario
**Snippet:** `snippets/performance/large_1k.py` (P01)

**Expected result:** Quick-fix is done in <300 ms.

**Actual:**  exactly as expected

**Status:**  PASS 
