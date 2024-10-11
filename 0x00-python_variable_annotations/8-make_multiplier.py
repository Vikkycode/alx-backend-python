#!/usr/bin/env python3
""" make mulplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function """
    def multiplier_function(value: float) -> float:
        """ function"""
        return value * multiplier
    return multiplier_function
