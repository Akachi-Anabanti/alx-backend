#!/usr/bin/env python3
"""A script that defines a function index"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of size two containing a start index
    and end index corresponding to the range of indexes to
    give back in a list for the particular pagination"""

    if page == 1:
        return 0, page_size
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns the page of with the page range"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, stop = index_range(page, page_size)

        print(start)
        print(stop)
        try:
            data = self.dataset()
            return data[start:stop]
        except IndexError:
            return []
