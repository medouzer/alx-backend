#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """function index_range"""
    total = page * page_size
    return (total - page_size, total)
