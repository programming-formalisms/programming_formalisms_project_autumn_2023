---
name: Create new class
about: Need to create a new class
title: 'Create [name_of_class]'
labels: ''
assignees: ''

---

In the class list, the class in the title
is mentioned. Create it!

# Procedure

 * [ ] Create a file for the class implementation
   with name `src/[module_name]/[class_name].py`,
   e.g. `src/pfpa2023/duck.py`
 * [ ] Create a file for the class tests,
   with name `tests/test_[class_name].py`,
   e.g. `tests/test_duck.py`
 * [ ] Create a minimal class implementation,
   for example:

```python
"""A duck."""

class Duck:

    """Duck is a duck."""
```

 * [ ] Create a minimal class test,
   for example:

```python
"""Tests all function in src.pf_example.duck."""
import unittest

from src.pf_example.duck import (
    Duck,
)


class TestDuck(unittest.TestCase):

    """Class to test the code in src.pf_example.duck."""

    def test_can_create_params(self):
        """#[issue_number]: Can create a Duck."""
        Duck()
```

The test is that it works, not that it does anything useful.

Use [the workflow that fits you best](https://github.com/programming-formalisms/programming_formalisms_example_project/tree/main/workflow#github-workflows), 
ideally use a topic branch for this issue 
and merge to develop using a PR with code review.

