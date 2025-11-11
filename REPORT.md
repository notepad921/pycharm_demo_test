# Test Report — PyCharm Quick‑Fix “Add superclass call”

Status values: **PASS / FAIL / N/A**.

## Summary
- Total scenarios: 18
- PASS: _n_
- FAIL: _n_
- N/A: _n_

## Matrix

### B01 — Single inheritance, no args
**Snippet:** `snippets/basic.py` (section B01)
- Expected: inspection triggers; `super().__init__()` inserted (position flexible but before dependent logic).
- Actual: 
- Status: 
- Diff (if FAIL):
```diff
```

### B02 — Positional + default
**Snippet:** `snippets/basic.py` (section B02)
- Expected: `super().__init__(x, y)`; keep `self.y` after call; formatting intact.
- Actual: 
- Status: 
```diff
```

### B03 — Keyword‑only
**Snippet:** `snippets/basic.py` (section B03)
- Expected: `super().__init__(limit=limit)`; docstring remains first.
- Actual: 
- Status: 
```diff
```

### B04 — Positional‑only (PEP 570)
**Snippet:** `snippets/basic.py` (section B04)
- Expected: `super().__init__(x, y)` (x positional).
- Actual: 
- Status: 
```diff
```

### B05 — Varargs passthrough
**Snippet:** `snippets/basic.py` (section B05)
- Expected: `super().__init__(*args, **kwargs)`; do not pass `a`.
- Actual: 
- Status: 
```diff
```

### B06 — Param names differ
**Snippet:** `snippets/basic.py` (section B06)
- Expected: `super().__init__(active=active, **kw)`; do not guess `uid→user_id`.
- Actual: 
- Status: 
```diff
```

### B07 — Built‑in parent
**Snippet:** `snippets/basic.py` (section B07)
- Expected: `super().__init__(iterable)`.
- Actual: 
- Status: 
```diff
```

### B08 — Exception subclass
**Snippet:** `snippets/basic.py` (section B08)
- Expected: `super().__init__(msg)`.
- Actual: 
- Status: 
```diff
```

### M01 — Diamond, cooperative
**Snippet:** `snippets/multiple.py` (section M01)
- Expected: uses `super().__init__(...)`, not `Base.__init__`.
- Actual:
- Status:
```diff
```

### M02 — Mixin without __init__
**Snippet:** `snippets/multiple.py` (section M02)
- Expected: inspection triggers and `super().__init__(x)` offered.
- Actual:
- Status:
```diff
```

### M03 — Base without __init__
**Snippet:** `snippets/multiple.py` (section M03)
- Expected: no inspection / proposal.
- Actual:
- Status:
```diff
```

### M04 — Explicit parent call already present
**Snippet:** `snippets/multiple.py` (section M04)
- Expected: inspection silent; no quick‑fix.
- Actual:
- Status:
```diff
```

### D01 — Parent is @dataclass
**Snippet:** `snippets/dataclasses.py` (section D01)
- Expected: `super().__init__(id=id, name=name)`.
- Actual:
- Status:
```diff
```

### D02 — Child is @dataclass, no explicit __init__
**Snippet:** `snippets/dataclasses.py` (section D02)
- Expected: no inspection (init generated).
- Actual:
- Status:
```diff
```

### T01 — Docstring first
**Snippet:** `snippets/typing_fmt.py` (section T01)
- Expected: call inserted after docstring.
- Actual:
- Status:
```diff
```

### T02 — Long signature, wrapping
**Snippet:** `snippets/typing_fmt.py` (section T02)
- Expected: wrapping/trailing comma preserved; call may be multiline.
- Actual:
- Status:
```diff
```

### T03 — Mutable default
**Snippet:** `snippets/typing_fmt.py` (section T03)
- Expected: `super().__init__(items)`.
- Actual:
- Status:
```diff
```

### E01 — Wrong decorators
**Snippet:** `snippets/edge.py` (section E01)
- Expected: inspection doesn’t confuse; no quick‑fix.
- Actual:
- Status:
```diff
```

### E02 — super in try/except
**Snippet:** `snippets/edge.py` (section E02)
- Expected: no inspection.
- Actual:
- Status:
```diff
```

### E03 — Metaclass/__new__
**Snippet:** `snippets/edge.py` (section E03)
- Expected: no proposal if parent lacks __init__.
- Actual:
- Status:
```diff
```
