#!/usr/bin/env python3
"""A script that defines a function index"""


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of size two containing a start index
    and end index corresponding to the range of indexes to
    give back in a list for the particular pagination"""

    if page == 1:
        return 0, page_size
    return (page - 1) * page_size, page * page_size
