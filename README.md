# PyCharm "Add superclass call" test report with code snippets

This repository collects small Python snippets that exercise PyCharm's inspection and quick-fix for missing calls to `super().__init__` in subclasses.  The files are meant to be opened directly in PyCharm while verifying the feature on Python 3.13 projects.

## Repository layout

| Path | Description |
| --- | --- |
| `README.md` | You are here. Overview of the repository and navigation tips. |
| `REPORT.md` | Consolidated test report that lists every scenario that was executed, the expected result, and the actual behaviour that was observed. |
| `snippets/` | Stand-alone Python modules grouped by scenario type. Each file is heavily commented so you can jump to a particular case quickly while testing inside PyCharm. |

### Snippet collections

- `snippets/basic_cases.py` &mdash; Happy-path scenarios for single inheritance and straightforward argument passing patterns.
- `snippets/dataclasses_cases.py` &mdash; Focuses on dataclasses and interactions with generated `__init__` methods.
- `snippets/edge_cases.py` &mdash; Negative scenarios where the inspection **must not** trigger (e.g., decorators, existing `super()` calls, metaclass tricks).
- `snippets/multiple_inheritance_cases.py` &mdash; Exercises method-resolution-order nuances when more than one parent class is involved.
- `snippets/performance/` &mdash; Large synthetic files (`large_1k.py`, `large_5k.py`) used to gauge responsiveness of bulk quick-fix operations.
- `snippets/readonly_case.py` &mdash; Tests behaviour in read-only files to ensure the IDE reports why the quick-fix cannot be applied.
- `snippets/typing_fmt_cases.py` &mdash; Cases that combine type hints, formatting, and quick-fix placement requirements.

Every snippet file starts with a docstring that explains the intention of the contained classes and includes inline comments with scenario identifiers (e.g., `B03`, `E02`).  The same identifiers are reused in `REPORT.md`, so you can cross-reference the written results with the code for testing it.

## How to use this repository

1. Open `REPORT.md` and review the verification I did.
2. Curious how those results were produced? Explore the `snippets/` directory to see the test cases codebase and short scenario notes.
3. The snippets can be useful if you want to re-check something.

## NB!
There are no true beautiful bug reports here, as the task was only to provide a list of test cases and a report on their completion.