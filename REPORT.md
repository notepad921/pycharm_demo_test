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
  Out of scope → global inspection settings, profiles, automation.

**Status legend:** PASS / FAIL

For **FAIL** I include a block with unexpected code after applying this quick-fix.

---

## B01 — Single inheritance, no args
**Snippet:** `snippets/basic_cases.py` (B01)  
**Steps:** Place caret on `ChildNoArgs.__init__` → Alt+Enter → *Add superclass call*.  
**Expected result:** Child inserts `super().__init__()`; formatting intact; earlier code is not allowed to rely on parent state before the call.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B02 — Positional + default
**Snippet:** `snippets/basic_cases.py` (B02)  
**Expected result:** Insert `super().__init__(x, y)` before `self.y = y`; formatting unchanged.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B03 — Keyword-only
**Snippet:** `snippets/basic_cases.py` (B03)  
**Expected result:** Insert `super().__init__(limit=limit)` after the docstring; the docstring remains the first statement.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B04 — Positional-only (PEP 570)
**Snippet:** `snippets/basic_cases.py` (B04)  
**Expected result:** Pass `x` positionally and not by name; insert `super().__init__(x, y)`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B05 — Varargs passthrough
**Snippet:** `snippets/basic_cases.py` (B05)  
**Expected result:** Forward only the variable arguments to the parent using `super().__init__(*args, **kwargs)` and do not pass the child-only parameter.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B06 — Param names differ
**Snippet:** `snippets/basic_cases.py` (B06)  
**Expected result:** Match parameters strictly by name (e.g., `active`) and forward the remainder via `**remaining_kwargs`; do not infer name mappings.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B07 — Built-in parent (list)
**Snippet:** `snippets/basic_cases.py` (B07)  
**Expected result:** Insert `super().__init__(iterable)` and preserve layout despite a C-implemented base.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B08 — Exception subclass
**Snippet:** `snippets/basic_cases.py` (B08)  
**Expected result:** Insert `super().__init__(msg)` so the exception message is propagated; no formatting regressions.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B09 — Parent uses __slots__
**Snippet:** `snippets/basic_cases.py` (B09)  
**Expected result:** Insert a parent call (e.g., `super().__init__(token=token)`) so that slot-backed attributes are initialized; formatting remains intact.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B10 — Built-in parent (dict)
**Snippet:** `snippets/basic_cases.py` (B10)  
**Expected result:** Insert `super().__init__(initial)` and keep indentation and spacing unchanged.  
**Actual:**  
**Status:**  

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
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B13 — Mixed positional-only + keyword-only
**Snippet:** `snippets/basic_cases.py` (B13)  
**Expected result:** Preserve argument kinds by passing positional-only arguments positionally and keyword-only by name, e.g., `super().__init__(x, y, flag=flag)`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B14 — Abstract Base Class (ABC)
**Snippet:** `snippets/basic_cases.py` (B14)  
**Expected result:** Insert `super().__init__(name)`; abstractness does not change call requirements.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B15 — Standard library class — threading.Thread
**Snippet:** `snippets/basic_cases.py` (B15)  
**Expected result:** Build a keyworded call reflecting provided arguments, e.g., `super().__init__(group=group, target=target, name=name)`; preserve formatting.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## B16 — Standard library class — logging.Logger
**Snippet:** `snippets/basic_cases.py` (B16)  
**Expected result:** Insert `super().__init__(name, level)` (or a keyworded variant) without altering layout.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

---

## M01 — Diamond, cooperative
**Snippet:** `snippets/multiple_inheritance_cases.py` (M01)  
**Expected result:** Prefer a cooperative `super().__init__(x)` call rather than addressing a specific base directly.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## M02 — Mixin without __init__
**Snippet:** `snippets/multiple_inheritance_cases.py` (M02)  
**Expected result:** Offer the quick-fix and insert `super().__init__(x)` according to MRO even if one of the bases has no `__init__`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## M03 — Base without __init__
**Snippet:** `snippets/multiple_inheritance_cases.py` (M03)  
**Expected result:** Do not raise an inspection and do not offer a quick-fix when the nearest MRO parents do not define `__init__`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## M04 — Explicit parent call already present
**Snippet:** `snippets/multiple_inheritance_cases.py` (M04)  
**Expected result:** Stay silent (no inspection, no quick-fix) when the child already calls a parent initializer explicitly.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

---

## D01 — Parent is @dataclass
**Snippet:** `snippets/dataclasses_cases.py` (D01)  
**Expected result:** Construct a keyworded call to the dataclass parent initializer, e.g., `super().__init__(id=id, name=name)`; keep any docstring first.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## D02 — Child is @dataclass (auto-generated __init__)
**Snippet:** `snippets/dataclasses_cases.py` (D02)  
**Expected result:** Do not show the inspection when the child relies on the dataclass-generated `__init__`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## D03 — Dataclass parent kw_only=True
**Snippet:** `snippets/dataclasses_cases.py` (D03)  
**Expected result:** Use a keyworded call to respect keyword-only dataclass fields, e.g., `super().__init__(id=id, name=name)`; no positional passing.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## D04 — Dataclass parent with slots/frozen
**Snippet:** `snippets/dataclasses_cases.py` (D04)  
**Expected result:** Insert a keyworded call such as `super().__init__(id=id)` and keep formatting intact even with `slots`/`frozen`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

---

## T01 — Docstring first
**Snippet:** `snippets/typing_fmt_cases.py` (T01)  
**Expected result:** Place the inserted call immediately after the docstring without reflowing it.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## T02 — Long signature, wrapping
**Snippet:** `snippets/typing_fmt_cases.py` (T02)  
**Expected result:** Preserve multi-line wrapping and trailing comma in the signature and body; the inserted call may be multi-line but must not reformat the function.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## T03 — Mutable default
**Snippet:** `snippets/typing_fmt_cases.py` (T03)  
**Expected result:** Insert `super().__init__(items)` and keep the indentation and layout unchanged.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## T04 — Multiline docstring (Google/Numpy)
**Snippet:** `snippets/typing_fmt_cases.py` (T04)  
**Expected result:** Insert the call after the multiline docstring block and do not modify docstring formatting.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## T05 — Comments around insertion point
**Snippet:** `snippets/typing_fmt_cases.py` (T05)  
**Expected result:** Keep surrounding comments intact and insert the call between them without altering spacing.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

---

## E01 — Wrong decorators
**Snippet:** `snippets/edge_cases.py` (E01)  
**Expected result:** Do not offer a quick-fix when `__init__` is decorated incorrectly (e.g., `@staticmethod`).  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## E02 — super in try/except
**Snippet:** `snippets/edge_cases.py` (E02)  
**Expected result:** Do not raise an inspection when a `super()` call already exists inside a `try/except` block.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## E03 — Metaclass / __new__
**Snippet:** `snippets/edge_cases.py` (E03)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the parent defines only `__new__` and no `__init__`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## E04 — Parent is object
**Snippet:** `snippets/edge_cases.py` (E04)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the only parent is `object`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## E05 — Parent defines __init__ = object.__init__
**Snippet:** `snippets/edge_cases.py` (E05)  
**Expected result:** Do not raise an inspection or offer a quick-fix when the parent explicitly aliases `__init__` to `object.__init__`.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

## E06 — Conditional super() already present
**Snippet:** `snippets/edge_cases.py` (E06)  
**Expected result:** Do not raise an inspection when a `super()` call is already present under a condition.  
**Actual:**  
**Status:**  

```incorrect code after applying
```

