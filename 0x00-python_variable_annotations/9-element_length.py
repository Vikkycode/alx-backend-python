#!/usr/bin/env python3
""" element """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ fun """
    return [(i, len(i)) for i in lst]
