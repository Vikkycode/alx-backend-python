#!/usr/bin/env python3
"""test utils module."""


def a_method(self):
    return 42

@memoize
def a_property(self):
    return self.a_method()
