#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


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
        """Dataset with deletion-resilient hypermedia pagination
        """
        assert isinstance(index, int) and index >= 0\
                                      and index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.__indexed_dataset
        dataset_size = len(indexed_dataset)
        data = []
        next_index = index
        for _ in range(page_size):
            while next_index < dataset_size\
                  and indexed_dataset.get(next_index) is None:
                next_index += 1
            if next_index < dataset_size:
                data.append(indexed_dataset[next_index])
                next_index += 1
            else:
                break

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
