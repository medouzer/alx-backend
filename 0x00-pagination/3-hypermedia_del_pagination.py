#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """method get_hyper_index"""
        all_data = self.indexed_dataset()
        index = 0 if index is None else index
        assert index is not None and index >= 0\
            and index <= max(all_data.keys())
        next_index = min(index + page_size, max(all_data.keys()))
        data = []
        current_index = index
        collected_items = 0
        while collected_items < page_size and current_index < len(all_data):
            if current_index in all_data:
                data.append(all_data[current_index])
                collected_items += 1
            current_index += 1
        next_index = current_index if current_index < len(all_data) else None
        return {'index': index, 'data': data,
                'page_size': page_size, 'next_index': next_index}
