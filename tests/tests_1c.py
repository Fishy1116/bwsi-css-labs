import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_all_negative_numbers():
    assert max_subarray_sum([-3, -2, -1]) == -1  # Test for all negative numbers

def test_all_positive_numbers():
    assert max_subarray_sum([1, 2, 3]) == 6  # Test for all positive numbers

def test_mixed_numbers():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # Test for mixed numbers

def test_single_element():
    assert max_subarray_sum([5]) == 5  # Test for single element

def test_empty_list():
    with pytest.raises(IndexError):
        max_subarray_sum([])  # Test for empty list