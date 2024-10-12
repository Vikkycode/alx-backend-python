#!/usr/bin/env python3
from typing import TypeVar, Mapping, Optional
""" safely get value function"""
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[str, T],
        key: str,
        default: Optional[T] = None) -> Optional[T]:
    """ annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
