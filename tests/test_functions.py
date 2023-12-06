import pytest
from solutions.two_d_lists import *

def test_get_row_count():
    assert get_row_count([[1, 2], [3, 4], [5, 6]]) == 3
    assert get_row_count([[]]) == 1
    assert get_row_count([]) == 0

def test_get_column_count():
    assert get_column_count([[1, 2], [3, 4], [5, 6]]) == 2
    assert get_column_count([[1], [2], [3]]) == 1
    assert get_column_count([[]]) == 0

def test_get_element():
    assert get_element([[1, 2], [3, 4]], 0, 1) == 2
    assert get_element([[1, 2], [3, 4]], 1, 0) == 3

def test_sum_two_d_list():
    assert sum_two_d_list([[1, 2], [3, 4]]) == 10
    assert sum_two_d_list([[1], [2], [3]]) == 6
    assert sum_two_d_list([[]]) == 0

def test_print_rows(capsys):  # capsys is a pytest fixture that captures stdout and stderr
    print_rows([[1, 2], [3, 4]])
    captured = capsys.readouterr()
    assert captured.out == "[1, 2]\n[3, 4]\n"

def test_contains_value():
    assert contains_value([[1, 2], [3, 4]], 3) == True
    assert contains_value([[1, 2], [3, 4]], 5) == False

def test_append_to_sublists():
    matrix = [[1], [1, 2], [1, 2, 3]]
    append_to_sublists(matrix, 99)
    assert matrix == [[1, 99], [1, 2, 99], [1, 2, 3, 99]]

def test_replace_in_two_d_list():
    matrix = [[1, 2], [2, 3], [4, 2]]
    replace_in_two_d_list(matrix, 2, 99)
    assert matrix == [[1, 99], [99, 3], [4, 99]]

def test_first_elements():
    assert first_elements([[1, 2], [3, 4], [5, 6]]) == [1, 3, 5]
    assert first_elements([[7], [8], [9]]) == [7, 8, 9]
    assert first_elements([[]]) == []

def test_even_elements_sublists():
    assert even_elements_sublists([[1, 2, 3], [4, 5, 6, 7]]) == [[1, 3], [4, 6]]
    assert even_elements_sublists([[1], [2], [3]]) == [[1], [2], [3]]
    assert even_elements_sublists([[]]) == [[]]

def test_concatenate_sublists():
    assert concatenate_sublists([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert concatenate_sublists([[7], [8], [9]]) == [7, 8, 9]
    assert concatenate_sublists([[]]) == []
