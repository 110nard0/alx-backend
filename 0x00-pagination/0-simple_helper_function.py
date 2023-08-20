#!/usr/bin/env python3
"""0-simple_helper_function Module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start index and end index of a particular page

    Args:
        page (int): page number
        page_size (int): size of page

    Returns:
        (tuple) containing indexes related to specific pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)
