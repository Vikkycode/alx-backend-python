#!/usr/bin/env python3
from typing import Sequence, TypeVar, Optional
""" safe first element function"""
T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Optional[T]:
    """ function """
    if lst:
        return lst[0]
    else:
        return None
