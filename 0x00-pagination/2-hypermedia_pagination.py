#!/usr/bin/env python3
"""Hypermedia pagination"""

from typing import Tuple, List
import csv
import math


def index_range(page, page_size) -> Tuple[int, int]:
    """function index_range"""
    total = page * page_size
    return (total - page_size, total)


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
        """method get_page"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        indexes = index_range(page, page_size)
        all_list = self.dataset()
        return all_list[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method get_hyper"""
        data = self.get_page(page, page_size)
        all_list = self.dataset()
        total_data = len(all_list)
        if (total_data / page_size) > page:
            next_page = page + 1
        else:
            next_page = None
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        total_pages = math.ceil(total_data / page_size)
        return {'page_size': page_size, 'page': page, 'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': int(total_pages)}
