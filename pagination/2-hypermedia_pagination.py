#!/usr/bin/env python3
"""module contains class Server and his differents methods"""
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset that is loaded from a CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieving a specific page of data from the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start is None or end is None:
            return []

        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """method that's gonnz returns a dictionary containing the
        following key-value pairs"""
        data = self.get_page(page, page_size)
        next_page = None
        prev_page = None
        total_pages = len(self.dataset()) // page_size

        if page < total_pages:
            next_page = page + 1

        if page > 1:
            prev_page = page - 1

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
