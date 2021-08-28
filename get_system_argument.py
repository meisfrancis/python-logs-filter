#!/usr/bin/env python3
import sys


def get_args(index, default=None):
    if index >= len(sys.argv):
        return default
    return sys.argv[index]

